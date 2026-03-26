from fastapi import FastAPI, UploadFile, File, HTTPException, WebSocket, WebSocketDisconnect
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from src.functions import image_name, info
from src.cnn_model import load_model
from database.animal_information import class_names
from logger import logging
from src.grok import client as groq_client
from aws.download import download_from_s3
import os

model = None 
device = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    global model, device
    try:
        os.makedirs("model", exist_ok=True)

        model_path = os.path.join("model", "inital_model.pth")
        
        if not os.path.exists(model_path):
            download_from_s3(
                bucket_name="animal-prediction",
                s3_file_anme="models/model.pth",
                local_file_path=model_path
            )

        model, device = load_model(model_path, num_classes=90)

        logging.info("Model loaded successfully.")

    except Exception as e:
        logging.error(f"FATAL: Model failed to load: {e}")
        raise

    yield

    del model
    logging.info("Model unloaded.")


app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["chrome-extension://*"],
    allow_methods=["POST", "GET"],
    allow_headers=["*"],
)


@app.get("/")
async def health():
    return {
        "status": "running",
        "model_loaded": model is not None,
        "device": str(device)
    }


@app.post("/predict")
async def predict(image: UploadFile = File(...)):
    try:
        if not image.content_type or not image.content_type.startswith("image/"):
            raise HTTPException(status_code=400, detail="File must be an image.")


        prob_list, out_list = await image_name(image, model, device)

        if not prob_list or not out_list:
            raise HTTPException(status_code=422, detail="Model returned empty predictions.")

        final_conf = prob_list[0] if isinstance(prob_list, list) else prob_list
        final_idx  = out_list[0]  if isinstance(out_list, list)  else out_list

        main_info, _ = info(out_list, prob_list)

        return {
            "class":      str(class_names[int(final_idx)]),
            "confidence": float(final_conf),
            "info":       str(main_info),
        }

    except HTTPException:
        raise

    except Exception as e:
        logging.error(f"/predict failed: {e}")
        return JSONResponse(status_code=500, content={"detail": "Internal server error."})

SYSTEM_PROMPT = (
    "You are an expert wildlife assistant. "
    "Answer questions about animals clearly and concisely."
)

@app.websocket("/query/{session_id}")
async def question(websocket: WebSocket, session_id: str):
    await websocket.accept()
    logging.info(f"WebSocket session opened: {session_id}")

    history = [{"role": "system", "content": SYSTEM_PROMPT}]

    try:
        while True:
            user_input = await websocket.receive_text()

            if not user_input.strip():
                await websocket.send_text("[error] Empty message.")
                continue

            history.append({"role": "user", "content": user_input})
            full_response = ""

            try:
                stream = await groq_client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=history,
                    stream=True,
                )

                async for chunk in stream:
                    if not chunk.choices:
                        continue
                    content = chunk.choices[0].delta.content
                    if content:
                        await websocket.send_text(content)
                        full_response += content

                history.append({"role": "assistant", "content": full_response})
                await websocket.send_text("[END]")

            except Exception as groq_err:
                logging.error(f"Groq API error in session {session_id}: {groq_err}")
                await websocket.send_text("[error] AI service failed. Please try again.")

    except WebSocketDisconnect:
        logging.info(f"WebSocket session closed: {session_id}")

    except Exception as e:
        logging.error(f"Unexpected WebSocket error in session {session_id}: {e}")
        try:
            await websocket.send_text("[error] Connection error. Please reconnect.")
            await websocket.close()
        except Exception:
            pass