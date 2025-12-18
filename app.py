from fastapi import FastAPI, UploadFile, File, HTTPException, Request
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from functions.functions import image_name, info
from database.animal_information import class_names

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/predict")
async def predict(image: UploadFile = File(...)):
    try:
        prob_list, out_list = await image_name(image)

        def get_number(data):
            if isinstance(data, list):
                return get_number(data[0])
            return data

        final_conf = get_number(prob_list)
        final_idx = get_number(out_list)

        main_info, _ = info(out_list, prob_list)

        return {
            "class": str(class_names[int(final_idx)]),
            "confidence": float(final_conf),
            "info": str(main_info)
        }
    except Exception as e:
        import traceback
        print(f"DEBUG ERROR: {traceback.format_exc()}")
        return JSONResponse(status_code=500, content={"detail": str(e)})

if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)