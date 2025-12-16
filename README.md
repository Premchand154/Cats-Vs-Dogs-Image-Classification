# Cats vs Dogs Image Classification using CNN & FastAPI

This project implements a **Convolutional Neural Network (CNN)** to classify images as **Cat** or **Dog** and deploys the trained model as a **REST API using FastAPI**.

The API accepts image uploads and returns the **predicted class along with a confidence score**, demonstrating an end-to-end deep learning deployment workflow.

---

# Project Overview

Image classification is a fundamental computer vision task.  
This project focuses on building a **binary image classifier** using deep learning and making it accessible via a backend API.

Key highlights:
- CNN model trained on Cats vs Dogs dataset
- Image preprocessing and normalization
- Model deployment using FastAPI
- Real-time predictions through REST API

---

# Model Details

- **Architecture:** CNN (MobileNetV2-based)
- **Input Size:** 150 × 150 × 3
- **Output:** Binary classification (Cat / Dog)
- **Activation:** Sigmoid
- **Loss Function:** Binary Cross-Entropy

---

# Features

- FastAPI-based REST API
- Image upload support
- Confidence-based predictions
- Production-style model loading
- Swagger UI for testing

---

# Project Structure

```

Cats-Vs-Dogs-CNN-FastAPI/
│
├── app.py                         # FastAPI application
├── requirements.txt               # Dependencies
├── Cats_Vs_Dogs_CNN.ipynb          # Model training notebook
├── models/
│   └── cats_vs_dogs_mobilenetv2.h5 # Trained CNN model
└── README.md

````

---

# Installation & Setup

# Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/Cats-Vs-Dogs-Image-Classification.git
cd Cats-Vs-Dogs-Image-Classification
````

# Create and activate virtual environment

```bash
python -m venv .venv
.venv\Scripts\activate    # Windows
```

# Install dependencies

```bash
pip install -r requirements.txt
```

---

# Run the Application

```bash
uvicorn app:app --reload
```

Server will start at:

```
http://127.0.0.1:8000
```

---

# API Usage

# Swagger UI

Open:

```
http://127.0.0.1:8000/docs
```

# Sample Prediction

Upload an image (cat or dog).

# Sample Response

```json
{
  "prediction": "Dog",
  "confidence": 0.94
}
```

---

# Model Limitation

* The model is a **single-label classifier**
* If an image contains **both a cat and a dog**, the model predicts the **dominant object**
* Handling multiple objects would require **object detection models (YOLO, SSD, etc.)**

---

# Technologies Used

* Python
* TensorFlow / Keras
* FastAPI
* NumPy
* Pillow
* Uvicorn

---

# Future Improvements

* Object detection for multi-animal images
* Cloud deployment (Render / AWS)
* Streamlit frontend
* Batch image prediction

---


