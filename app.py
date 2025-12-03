from fastapi import FastAPI, UploadFile, File, HTTPException, Request
from fastapi.responses import JSONResponse
from functions.functions import info, image_name

app = FastAPI()

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={
            "status": 500,
            "error": "Internal Server Error",
            "detail": str(exc)
        }
    )

@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "status": exc.status_code,
            "error": exc.detail,
            "detail": "Request could not be processed"
        }
    )


@app.get("/")
def root():
    return {"msg": "animal prediction model"}


@app.post("/predict")
async def predict(image: UploadFile = File(...)):
    try:
        prob, out = image_name(image)
        return {
            "class": out,
            "confidence": float(prob)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/info")
def get_info(class_name: str):
    try:
        return {
            "info": info(class_name)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
