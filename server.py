"""
Waste Sense - FastAPI Backend for YOLO26s best.pt
Run with: uvicorn server:app --host 0.0.0.0 --port 8000
"""
import io
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from ultralytics import YOLO
from PIL import Image

app = FastAPI(title="Waste Sense API", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

model = YOLO("best.pt")

@app.get("/")
def root():
    return {"status": "ok", "model": "best.pt", "classes": model.names}

@app.post("/predict")
async def predict(file: UploadFile = File(...), conf: float = 0.40, iou: float = 0.45, imgsz: int = 640):
    img = Image.open(io.BytesIO(await file.read())).convert("RGB")
    res = model.predict(img, conf=conf, iou=iou, imgsz=imgsz, verbose=False)[0]
    dets = []
    for b in res.boxes:
        x1, y1, x2, y2 = b.xyxy[0].tolist()
        dets.append({
            "bbox": [x1, y1, x2, y2],
            "classid": int(b.cls[0]),
            "classname": model.names[int(b.cls[0])],
            "confidence": float(b.conf[0]),
        })
    return JSONResponse({"detections": dets, "imagesize": list(img.size)})
