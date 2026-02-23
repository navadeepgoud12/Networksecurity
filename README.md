### Network security project
# 🛡️ Network Security - Phishing Detection System

## 📌 Overview

This project is an end-to-end **Machine Learning-based Network Security system** that detects whether a website is **phishing or legitimate**.

It uses various URL-based features and a trained ML model to classify websites and is deployed using **FastAPI on Render**.

---

## 🚨 Problem Statement

Phishing attacks are one of the most dangerous cyber threats where attackers create fake websites to steal sensitive user information.

This system helps to:

* Detect malicious websites
* Prevent cyber fraud
* Automate security checks using ML

---

## ⚙️ Features

* 🔍 Phishing detection using ML
* ⚡ FastAPI backend
* 📊 End-to-end ML pipeline
* 📁 CSV-based prediction input
* 📦 Docker support
* ☁️ Deployed on Render
* 📘 Swagger UI for API testing

---

## 🧠 Tech Stack

* Python 🐍
* FastAPI ⚡
* Scikit-learn 🤖
* Pandas 📊
* MLflow 📈
* Docker 🐳
* Uvicorn 🚀

---

## 📂 Project Structure

```bash
NETWORK_SECURITY/
│
├── .github/workflows/      # CI/CD pipeline
├── data_schema/            # Data schema validation
├── final_model/            # Trained model files
├── logs/                   # Logging files
├── Network_Data/           # Raw data
├── networksecurity/        # Core ML pipeline code
├── notebooks/              # EDA & experimentation
├── prediction_output/      # Prediction results
├── templates/              # HTML templates (if any)
├── valid_data/             # Validated data
│
├── app.py                  # FastAPI app
├── main.py                 # Entry point
├── push_data.py            # Data ingestion script
├── requirements.txt        # Dependencies
├── Dockerfile              # Docker config
├── .env                    # Environment variables
└── README.md               # Documentation
```

---

## 🚀 Getting Started

### 🔧 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

---

### 🧪 2. Create Virtual Environment

#### ▶️ Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### ▶️ Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 📦 3. Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

### 🔐 4. Setup Environment Variables

Create a `.env` file in the root directory and add:

```env
MLFLOW_TRACKING_URI=your_mlflow_uri
MLFLOW_TRACKING_USERNAME=your_username
MLFLOW_TRACKING_PASSWORD=your_password
```

---

## ▶️ Running the Application Locally

```bash
uvicorn main:app --reload
```

Open browser:

```
http://127.0.0.1:8000/docs
```

👉 You will see Swagger UI to test APIs.

---

## 🔗 API Endpoints

### 🔹 GET /

* Health check endpoint

### 🔹 GET /train

* Trains the ML model

### 🔹 POST /predict

* Accepts CSV file
* Returns prediction (Phishing / Legitimate)

---

## 🐳 Running with Docker

### Build Docker Image

```bash
docker build -t network-security .
```

### Run Container

```bash
docker run -p 8000:8000 network-security
```

---

## ☁️ Deployment (Render)

This project is deployed on **Render** using FastAPI.

### Steps followed:

1. Pushed code to GitHub
2. Connected GitHub repo to Render
3. Selected **Web Service**
4. Added build command:

```bash
pip install -r requirements.txt
```

5. Start command:

```bash
uvicorn main:app --host 0.0.0.0 --port 10000
```

---

## 📸 API Preview

FastAPI provides automatic interactive API docs:

```
/docs
```

---

## 📈 Future Improvements

* Add frontend UI (Flask / React)
* Real-time URL input instead of CSV
* Improve model accuracy
* Add authentication system

---

## 👨‍💻 Author

**Navadeep Goud**

---

## ⭐ Conclusion

This project demonstrates how Machine Learning and FastAPI can be used together to build a real-world **cybersecurity solution** for phishing detection. 

vist servie https://networksecurity-of6m.onrender.com

---
git add 