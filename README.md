# 🐾 Circle Search AI

An end-to-end AI-powered visual search system that allows users to capture any region of their screen, classify objects using a deep learning model, and interact with an AI assistant for additional insights.

---

## 🚀 Overview

Circle Search AI is a full-stack project combining:

* **Machine Learning (PyTorch)** for image classification
* **FastAPI backend** for inference and AI interaction
* **Chrome Extension (Manifest v3)** for real-time screen capture
* **AWS (EC2 + S3)** for deployment and model storage
* **Docker** for containerized deployment

---

## ✨ Features

* 🔍 Capture any part of the screen directly from the browser
* 🧠 Classify objects using a trained CNN model
* 📊 Confidence score + contextual information
* 🤖 Real-time AI chat (Grok API via WebSocket)
* ☁️ Model loaded dynamically from AWS S3
* 🐳 Fully containerized using Docker

---

## 🏗️ Architecture

```text
Chrome Extension (content.js)
        ↓
FastAPI Backend (EC2)
        ↓
PyTorch Model (S3)
        ↓
Grok API (WebSocket)
```

---

## ⚙️ Tech Stack

* **Frontend**: Chrome Extension (JavaScript, Manifest v3)
* **Backend**: FastAPI (Python)
* **ML**: PyTorch (EfficientNet-based CNN)
* **Cloud**: AWS EC2, S3
* **DevOps**: Docker
* **AI Integration**: Grok API (WebSocket streaming)

---

## 📦 Project Structure

```bash
.
├── app.py
├── dockerfile
├── requirement.txt
├── src/
│   ├── cnn_model.py
│   ├── functions.py
│   └── grok.py
├── aws/
│   ├── upload.py
│   └── download.py
├── extension/
│   ├── background.js
│   ├── content.js
│   ├── manifest.json
│   └── popup.html
├── model/
├── logs/
└── database/
```

---

## 🧪 How It Works

1. User activates the Chrome extension
2. Selects an area on the screen
3. Screenshot is sent to FastAPI backend
4. Model predicts object class + confidence
5. Result is displayed in UI
6. User can interact with AI (WebSocket-based chat)

---

## 🐳 Docker Setup

```bash
docker build -t animal .
docker run -d -p 8000:8000 \
-e access_id=YOUR_ACCESS_KEY \
-e secret_key=YOUR_SECRET_KEY \
-e groq_api_key=YOUR_API_KEY \
--name animal-container animal
```

---

## ☁️ AWS Deployment

* Model stored in **S3 bucket**
* Backend deployed on **EC2 instance**
* Elastic IP used for public access
* IAM roles recommended instead of hardcoded keys

---

## ⚠️ Known Issues & Limitations

### 🔒 WebSocket Security Issue

When running on HTTPS websites (e.g., Google, YouTube):

* `ws://` connections are **blocked by the browser**
* `wss://` requires **SSL configuration on the server**

#### 🔧 Solution:

* Configure **Nginx + SSL (Let’s Encrypt)**
* Use `wss://your-domain/query/...` instead of `ws://`

---

### 🌐 CORS & Extension Context

* Chrome extensions run in isolated contexts
* Proper CORS configuration is required in FastAPI

---

### 💾 Disk Constraints (EC2)

* Default EBS volumes may be insufficient
* Requires manual resizing using:

  * `growpart`
  * `resize2fs`

---

## 🔐 Security Considerations

* Do NOT expose AWS credentials in code
* Use environment variables or IAM roles
* Rotate keys if leaked
* Use HTTPS in production

---

## 📈 Future Improvements

* Add HTTPS + WSS support (production-ready)
* Improve UI/UX of extension
* Add caching for model inference
* Optimize model size and latency
* Add authentication & rate limiting

---

## 🎯 Learning Outcomes

* Built a full-stack ML system from scratch
* Integrated browser extension with backend APIs
* Deployed scalable system on AWS
* Handled real-world issues:

  * WebSocket security (WSS)
  * Docker deployment
  * Cloud storage (S3)
  * Networking & CORS

---

## 🧑‍💻 Author

Arun
Aspiring AI/ML Engineer

---
