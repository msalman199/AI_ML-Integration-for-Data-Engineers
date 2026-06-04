# 🤖 ML Pipeline Integration 

<p align="center">

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![Scikit Learn](https://img.shields.io/badge/Scikit--Learn-ML-F7931E?style=for-the-badge\&logo=scikitlearn\&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-150458?style=for-the-badge\&logo=pandas\&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-Numerical%20Computing-013243?style=for-the-badge\&logo=numpy\&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-REST%20API-000000?style=for-the-badge\&logo=flask\&logoColor=white)
![Cron](https://img.shields.io/badge/Cron-Automation-orange?style=for-the-badge)
![Linux](https://img.shields.io/badge/Linux-Ubuntu-E95420?style=for-the-badge\&logo=ubuntu\&logoColor=white)
![MLOps](https://img.shields.io/badge/MLOps-Pipeline-blue?style=for-the-badge)

</p>

---

# 📖 Overview

This lab demonstrates how to build a complete **Machine Learning Pipeline** that automates:

* 📊 Data Generation
* 🧹 Data Processing
* 🤖 Model Training
* 📈 Model Evaluation
* 🚀 Model Deployment
* 🔄 Model Reloading
* ⏰ Scheduled Retraining

By the end of this lab, you will have a fully automated ML workflow running on a Linux machine.

---

# 🎯 Learning Objectives

After completing this lab, you will be able to:

✅ Integrate ML model training into ETL workflows

✅ Automate training using Cron jobs

✅ Deploy ML models using REST APIs

✅ Serve predictions in real-time

✅ Build end-to-end MLOps pipelines

---

# 🛠 Prerequisites

* Basic Python programming
* Linux command-line experience
* Understanding of ML concepts
* Familiarity with ETL workflows
* Basic knowledge of preprocessing techniques

---

# 🖥 Environment Setup

## 🔧 Step 1: Update System & Install Dependencies

```bash
sudo apt update
sudo apt install -y python3-pip python3-venv cron
```

---

## 📁 Step 2: Create Project Structure

```bash
mkdir -p ~/ml-pipeline/{data,models,scripts,logs}
cd ~/ml-pipeline
```

Project Layout:

```text
ml-pipeline/
│
├── data/
├── models/
├── scripts/
├── logs/
└── venv/
```

---

## 🐍 Step 3: Create Python Virtual Environment

```bash
python3 -m venv venv

source venv/bin/activate

pip install --upgrade pip

pip install scikit-learn pandas numpy joblib flask
```

---

# 🧠 Task 1: Build Automated Training Pipeline

---

## 📊 Step 1: Create Dataset Generator

Create:

```bash
scripts/generate_data.py
```

### Responsibilities

✔ Generate synthetic customer data

✔ Simulate churn behavior

✔ Create realistic business features

### Dataset Features

| Feature         | Description         |
| --------------- | ------------------- |
| age             | Customer age        |
| tenure          | Months with company |
| monthly_charges | Monthly bill        |
| total_charges   | Lifetime spending   |
| churn           | Target variable     |

---

### Pipeline Flow

```text
Generate Features
        │
        ▼
Create Churn Labels
        │
        ▼
Create DataFrame
        │
        ▼
Save CSV Dataset
```

Run:

```bash
python3 scripts/generate_data.py
```

---

## 🤖 Step 2: Create Model Training Script

Create:

```bash
scripts/train_model.py
```

### Training Workflow

```text
Load Dataset
      │
      ▼
Preprocess Data
      │
      ▼
Train/Test Split
      │
      ▼
Random Forest Training
      │
      ▼
Model Evaluation
      │
      ▼
Save Model
```

### Model Configuration

```python
RandomForestClassifier(
    n_estimators=100,
    random_state=42
)
```

---

### Evaluation Metrics

* Accuracy
* Precision
* Recall
* F1 Score

Run:

```bash
python3 scripts/train_model.py
```

---

## 💾 Step 3: Save Trained Models

Store models inside:

```text
models/
```

Example:

```text
model_20260604_020000.pkl
```

Create symbolic link:

```text
latest_model.pkl
```

Benefits:

✔ Easy deployment

✔ Automatic model versioning

✔ Quick rollback support

---

## 🔄 Step 4: Create Pipeline Orchestration Script

Create:

```bash
scripts/run_pipeline.sh
```

Responsibilities:

### 📦 Data Generation

```bash
generate_data.py
```

### 🤖 Model Training

```bash
train_model.py
```

### 📝 Logging

```bash
logs/pipeline.log
```

### ✅ Success Validation

Verify:

* Data created
* Model trained
* Model saved

Make executable:

```bash
chmod +x scripts/run_pipeline.sh
```

---

## ⏰ Step 5: Automate Training Using Cron

Open cron editor:

```bash
crontab -e
```

Daily training:

```cron
0 2 * * * /home/$USER/ml-pipeline/scripts/run_pipeline.sh
```

Testing schedule:

```cron
*/5 * * * * /home/$USER/ml-pipeline/scripts/run_pipeline.sh
```

Verify:

```bash
crontab -l
```

---

# 🚀 Task 2: Deploy Model for Inference

---

## 🌐 Step 1: Create Flask Model API

Create:

```bash
scripts/serve_model.py
```

### REST API Endpoints

| Endpoint | Method | Purpose             |
| -------- | ------ | ------------------- |
| /health  | GET    | Server status       |
| /predict | POST   | Model prediction    |
| /reload  | POST   | Reload latest model |

---

### API Architecture

```text
Client Request
        │
        ▼
Flask API
        │
        ▼
Load Model
        │
        ▼
Generate Prediction
        │
        ▼
JSON Response
```

---

### Example Prediction Request

```json
{
  "features": [35, 12, 65.5, 786.0]
}
```

Example Response:

```json
{
  "prediction": 1,
  "probability": 0.89
}
```

---

## ⚙ Step 2: Create Deployment Script

Create:

```bash
scripts/deploy_model.sh
```

Supported Commands:

### Start Server

```bash
./scripts/deploy_model.sh start
```

### Stop Server

```bash
./scripts/deploy_model.sh stop
```

### Restart Server

```bash
./scripts/deploy_model.sh restart
```

---

### Process Management

Store process ID:

```text
model_server.pid
```

Benefits:

✔ Easy stop/start

✔ Service monitoring

✔ Process tracking

---

## 🧪 Step 3: Create API Test Client

Create:

```bash
scripts/test_inference.py
```

Tests:

### Health Endpoint

```http
GET /health
```

### Prediction Endpoint

```http
POST /predict
```

Sample Features:

```python
[35, 12, 65.5, 786.0]
```

Run:

```bash
python3 scripts/test_inference.py
```

---

# 🔍 Verification

---

## ✅ Verify Dataset Generation

```bash
ls -lh data/
```

Expected:

```text
customer_data_*.csv
```

---

## ✅ Verify Model Training

```bash
python3 scripts/train_model.py
```

Expected:

```text
Accuracy: 0.85+
```

---

## ✅ Verify Model Storage

```bash
ls -lh models/
```

Expected:

```text
model_*.pkl
latest_model.pkl
```

---

## ✅ Verify Pipeline Execution

```bash
./scripts/run_pipeline.sh
```

Check logs:

```bash
cat logs/pipeline*.log
```

Expected:

```text
Data Generated
Training Started
Model Saved
Pipeline Completed
```

---

## ✅ Verify Cron Service

```bash
sudo systemctl status cron
```

Monitor:

```bash
tail -f logs/cron.log
```

---

## ✅ Verify API Deployment

Start service:

```bash
./scripts/deploy_model.sh start
```

Test API:

```bash
python3 scripts/test_inference.py
```

Expected:

```text
Health Status: OK

Prediction: Churn
Probability: 0.89
```

---

## ✅ Verify Model Reload

Retrain:

```bash
python3 scripts/train_model.py
```

Reload:

```bash
curl -X POST http://localhost:5000/reload
```

Expected:

```json
{
  "status": "success"
}
```

---

# 🛠 Troubleshooting

---

## ❌ Cron Job Not Running

Check:

```bash
sudo systemctl status cron
```

Validate:

```bash
crontab -l
```

Review:

```bash
grep CRON /var/log/syslog
```

---

## ❌ Flask Server Fails

Verify:

```bash
netstat -tuln | grep 5000
```

Check logs:

```bash
cat logs/model_server.log
```

---

## ❌ Import Errors

Activate environment:

```bash
source venv/bin/activate
```

Reinstall packages:

```bash
pip install scikit-learn pandas numpy joblib flask
```

---

## ❌ Model Not Found

Verify:

```bash
ls -lh models/
```

Check symlink:

```bash
ls -l models/latest_model.pkl
```

---

# 📚 Key Concepts Learned

## 🤖 Machine Learning

* Random Forest Classification
* Model Evaluation
* Inference APIs

## ⚙ MLOps

* Automated Training
* Model Versioning
* Deployment Automation

## ⏰ Automation

* Cron Scheduling
* Pipeline Orchestration
* Logging

## 🌐 Model Serving

* Flask APIs
* Health Checks
* Model Reloading

---

# 🌍 Real-World Applications

This architecture is commonly used for:

🏦 Customer Churn Prediction

🛒 Product Recommendation Systems

📈 Sales Forecasting

🏥 Healthcare Risk Prediction

🔐 Fraud Detection

📡 Predictive Monitoring Systems

---

# 🎓 Lab Conclusion

In this lab you successfully:

✅ Built an automated ML training pipeline

✅ Generated synthetic datasets

✅ Trained and evaluated machine learning models

✅ Automated retraining with Cron

✅ Deployed models using Flask APIs

✅ Created real-time inference services

✅ Implemented model reloading without downtime

This workflow represents a foundational MLOps architecture used across modern enterprise AI platforms.

---

# 🚀 Next Steps

* Add Docker containerization
* Integrate MLflow experiment tracking
* Implement model monitoring
* Deploy to Kubernetes
* Add CI/CD automation
* Integrate cloud storage (AWS S3)
* Implement A/B model testing
* Add Prometheus & Grafana monitoring

---

# 🏆 Lab Complete

You now have hands-on experience building a complete **Machine Learning Pipeline Integration System** that automates data generation, model training, deployment, and inference in a production-style workflow.

**Happy Learning & Building! 🚀**
