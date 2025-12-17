# Cats vs Dogs Image Classification

# CNN + FastAPI + Web UI

This project implements an **end-to-end deep learning image classification system** that distinguishes between **cats and dogs** using a **Convolutional Neural Network (CNN)** and exposes predictions through a **FastAPI REST API** with a **simple web-based frontend**.

Users can upload an image and instantly receive the **predicted class along with a confidence score**, demonstrating a complete **ML → API → Frontend deployment workflow**.

---

# Project Overview

Image classification is a core computer vision problem.
This project demonstrates how to:

* Train a **binary image classifier** using deep learning
* Serve the trained model via **FastAPI**
* Consume the API using a **lightweight HTML/CSS/JavaScript frontend**
* Deliver real-time predictions through a clean UI

---

# Model Details

* **Architecture:** MobileNetV2-based CNN
* **Input Size:** `150 × 150 × 3`
* **Output:** Binary classification (Cat / Dog)
* **Activation Function:** Sigmoid
* **Loss Function:** Binary Cross-Entropy
* **Framework:** TensorFlow / Keras

---

# Features

* CNN-based image classification
* FastAPI REST API for inference
* Image upload support
* Confidence-based predictions
* Production-style model loading
* Interactive **Swagger UI**
* Simple **web frontend** for real-time testing

---

# Project Structure

```
Cats-Vs-Dogs-CNN-FastAPI/
│
├── app.py                          # FastAPI backend
├── requirements.txt                # Python dependencies
├── Cats_Vs_Dogs_CNN.ipynb           # Model training notebook
│
├── models/
│   └── cats_vs_dogs_mobilenetv2.h5  # Trained CNN model
│
├── frontend/
│   ├── index.html                  # Web UI
│   ├── style.css                   # Styling
│   └── script.js                   # API integration
│
└── README.md
```

---

# Installation & Setup

# Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Cats-Vs-Dogs-Image-Classification.git
cd Cats-Vs-Dogs-Image-Classification
```

---

# Create & Activate Virtual Environment

```bash
python -m venv .venv
.venv\Scripts\activate     # Windows
# source .venv/bin/activate  # Linux / Mac
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Application

# Start the FastAPI Server

```bash
uvicorn app:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

---

#  Using the Web Interface

1. Open `frontend/index.html` in your browser
2. Upload a **cat or dog image**
3. Click **Predict**
4. View the prediction and confidence score

The frontend communicates directly with the FastAPI backend.

---

# API Documentation (Swagger UI)

FastAPI provides built-in API documentation:

```
http://127.0.0.1:8000/docs
```

You can test image uploads directly from the browser.

---

# Sample API Response

```json
{
  "prediction": "Dog",
  "confidence": 94.0
}
```

---

# Model Limitations

* This is a **single-label classifier**
* If an image contains **both a cat and a dog**, the model predicts the **dominant object**
* Multiple-object handling would require **object detection models** such as:

  * YOLO
  * SSD
  * Faster R-CNN

---

# Technologies Used

* **Python**
* **TensorFlow / Keras**
* **FastAPI**
* **NumPy**
* **Pillow**
* **Uvicorn**
* **HTML / CSS / JavaScript**

---

# Future Improvements

* Object detection for multi-animal images
* Cloud deployment (AWS / Render / Railway)
* Dockerization
* Streamlit or React frontend
* Batch image prediction
* Model versioning and monitoring

---

