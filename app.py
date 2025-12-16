from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
import io

app = FastAPI(title="Cats vs Dogs CNN API")

model = None
IMG_SIZE = 150   # change if your model uses different size

@app.on_event("startup")
def load_cnn_model():
    global model
    model = load_model(r"D:\Machine Learning\Project 6 Cats Vs Dogs classification\models\cats_vs_dogs_mobilenetv2.h5")
    print("✅ CNN model loaded successfully")

def preprocess_image(image_bytes):
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    image = image.resize((IMG_SIZE, IMG_SIZE))
    image = np.array(image) / 255.0
    image = np.expand_dims(image, axis=0)
    return image

@app.get("/")
def home():
    return {"message": "Cats vs Dogs CNN API is running 🚀"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    image_bytes = await file.read()
    image = preprocess_image(image_bytes)

    prob = model.predict(image)[0][0]

    label = "Dog" if prob >= 0.5 else "Cat"
    confidence = prob if prob >= 0.5 else 1 - prob

    return JSONResponse({
        "prediction": label,
        "confidence": float(round(confidence, 2))
    })
