# 🚀 End-to-End AIOps System 

<div align="center">

# 🤖 End-to-End AIOps System

### Build a Complete AI-Powered Operations Platform with Apache Spark, ClickHouse, REST APIs, Monitoring & Predictive Analytics

![Linux](https://img.shields.io/badge/Linux-Ubuntu%2020.04+-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Apache Spark](https://img.shields.io/badge/Apache%20Spark-3.4.0-E25A1C?style=for-the-badge&logo=apachespark&logoColor=white)
![ClickHouse](https://img.shields.io/badge/ClickHouse-Latest-FFCC01?style=for-the-badge&logo=clickhouse&logoColor=black)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-REST%20API-000000?style=for-the-badge&logo=flask&logoColor=white)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-AIOps-FF6F00?style=for-the-badge&logo=scikitlearn&logoColor=white)

</div>

---

# 📖 Overview

Modern enterprise environments generate millions of operational events every day. Manual monitoring is no longer sufficient.

In this lab, you will build a complete **End-to-End AIOps Platform** capable of:

✅ Collecting operational metrics

✅ Processing streaming data with Apache Spark

✅ Storing time-series data in ClickHouse

✅ Exposing REST APIs

✅ Running automated workflows

✅ Monitoring infrastructure health

✅ Detecting anomalies

✅ Predicting future system behavior using AI

---

# 🎯 Learning Objectives

By completing this lab, you will learn how to:

- 🏗 Design a complete AIOps architecture
- 📥 Build a metrics ingestion pipeline
- ⚡ Process streaming data with Apache Spark
- 🗄 Store operational data in ClickHouse
- 🌐 Build REST APIs using Flask
- 🔄 Automate workflows and scheduling
- 🚨 Implement monitoring and alerting
- 🤖 Integrate machine learning predictions
- 🛡 Add recovery and resiliency mechanisms

---

# 🧰 Prerequisites

Before starting, ensure you have:

- Basic Linux command-line knowledge
- Python programming experience
- Understanding of REST APIs
- Basic SQL skills
- Familiarity with distributed systems concepts

---

# 🖥 System Requirements

| Resource | Requirement |
|-----------|-------------|
| OS | Ubuntu 20.04+ |
| RAM | 8 GB Minimum |
| Storage | 20 GB Free |
| CPU | 2+ Cores Recommended |
| Network | Internet Access |

---

# 🏗 AIOps Architecture

```text
                ┌────────────────────┐
                │  Metrics Sources   │
                └─────────┬──────────┘
                          │
                          ▼
                ┌────────────────────┐
                │ Data Ingestion     │
                └─────────┬──────────┘
                          │
                          ▼
                ┌────────────────────┐
                │ Apache Spark       │
                │ Processing Layer   │
                └─────────┬──────────┘
                          │
            ┌─────────────┴─────────────┐
            ▼                           ▼
 ┌───────────────────┐      ┌──────────────────┐
 │ ClickHouse DB     │      │ AI Predictor     │
 └─────────┬─────────┘      └─────────┬────────┘
           │                          │
           ▼                          ▼
      ┌──────────────────────────────────┐
      │ Flask REST API Server            │
      └───────────────┬──────────────────┘
                      │
                      ▼
      ┌──────────────────────────────────┐
      │ Monitoring & Alerting Engine     │
      └──────────────────────────────────┘
```

---

# ⚙️ Environment Setup

## 🔹 Step 1: Update System

```bash
sudo apt update && sudo apt upgrade -y
```

---

## 🔹 Step 2: Install Python

```bash
sudo apt install -y python3 python3-pip python3-venv git curl
```

---

## 🔹 Step 3: Install Java

Apache Spark requires Java.

```bash
sudo apt install -y openjdk-11-jdk
```

---

## 🔹 Step 4: Install Docker

```bash
curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker $USER

newgrp docker
```

---

## 🔹 Step 5: Create Project

```bash
mkdir -p ~/aiops-lab

cd ~/aiops-lab

python3 -m venv venv

source venv/bin/activate
```

---

## 🔹 Step 6: Install Python Packages

```bash
pip install pyspark==3.4.0 \
clickhouse-driver \
flask \
requests \
pandas \
numpy \
scikit-learn \
schedule
```

---

# 🗄 Deploy ClickHouse

## Start Database

```bash
docker run -d \
--name clickhouse-server \
-p 8123:8123 \
-p 9000:9000 \
--ulimit nofile=262144:262144 \
clickhouse/clickhouse-server:latest
```

---

## Verify Database

```bash
docker ps
```

Expected output:

```text
clickhouse-server
```

---

# 📂 Create Project Structure

```bash
mkdir -p {data,logs,models,config}

touch ingestion.py \
spark_processor.py \
db_manager.py \
api_server.py \
workflow.py \
monitor.py \
predictor.py \
main.py
```

---

# 📥 Task 1: Build Data Ingestion Layer

## Purpose

Generate operational metrics such as:

- CPU Usage
- Memory Usage
- Latency
- Error Rate
- Service Type

---

## File

```bash
ingestion.py
```

### Responsibilities

✅ Simulate production telemetry

✅ Generate JSON metric batches

✅ Save metrics into data directory

### Example Metric

```json
{
  "timestamp": "2026-06-01T12:00:00",
  "service": "web",
  "cpu_usage": 72.4,
  "memory_usage": 65.3,
  "latency_ms": 120,
  "error_rate": 1.4
}
```

---

# ⚡ Task 2: Apache Spark Processing

## File

```bash
spark_processor.py
```

### Responsibilities

- Read JSON metrics
- Apply schema
- Aggregate metrics
- Detect anomalies
- Export Parquet data

### Example Rules

```text
CPU > 80%
OR
Error Rate > 5%

=> Anomaly
```

---

# 🗄 Task 3: ClickHouse Integration

## File

```bash
db_manager.py
```

### Create Tables

### Raw Metrics Table

```sql
CREATE TABLE metrics
```

Stores:

- Timestamp
- Service
- CPU Usage
- Memory Usage
- Latency
- Error Rate

---

### Aggregated Metrics Table

```sql
CREATE TABLE aggregated_metrics
```

Stores:

- Avg CPU
- Max CPU
- Avg Memory
- Latency Metrics
- Error Totals
- Anomaly Status

---

# 🌐 Task 4: REST API Development

## File

```bash
api_server.py
```

---

## Health Endpoint

```http
GET /health
```

Example:

```json
{
  "status":"healthy",
  "service":"aiops-api"
}
```

---

## Metrics Endpoint

```http
GET /metrics
```

Returns recent metrics.

---

## Anomalies Endpoint

```http
GET /anomalies
```

Returns detected anomalies.

---

## Prediction Endpoint

```http
POST /predict
```

Request:

```json
{
  "service":"web"
}
```

Response:

```json
{
  "cpu":74.5,
  "memory":66.2,
  "latency":110
}
```

---

# 🔄 Task 5: Workflow Automation

## File

```bash
workflow.py
```

### Pipeline Flow

```text
Ingestion
    ↓
Spark Processing
    ↓
ClickHouse Storage
    ↓
Anomaly Detection
```

---

## Scheduler

Run every:

```text
5 Minutes
```

Cleanup:

```text
Daily
```

Retention:

```text
7 Days
```

---

# 🚨 Task 6: Monitoring & Alerts

## File

```bash
monitor.py
```

### Alert Thresholds

| Metric | Threshold |
|----------|----------|
| CPU | 80% |
| Memory | 85% |
| Latency | 400ms |
| Error Rate | 5% |

---

### Example Alert

```text
ALERT [CPU]

Web service exceeded CPU threshold
```

---

# 🤖 Task 7: AI Prediction Engine

## File

```bash
predictor.py
```

### Machine Learning Model

```text
RandomForestRegressor
```

---

### Features

- Hour
- Day of Week
- Service Type
- Previous Values
- Historical Trends

---

### Predictions

Forecast:

- CPU Usage
- Memory Usage
- Latency
- Error Rates

---

### Anomaly Detection

```text
Deviation > 30%

=> Flag Anomaly
```

---

# 🚀 Task 8: Main Orchestration

## File

```bash
main.py
```

### Launch Components

```text
✓ ClickHouse

✓ API Server

✓ Workflow Scheduler

✓ Monitoring Engine

✓ AI Predictor
```

---

# ✅ Verification

## Test Ingestion

```bash
python3 ingestion.py
```

---

## Verify Files

```bash
ls -lh data/
```

---

## Test Spark

```bash
python3 spark_processor.py
```

---

## Test Database

```bash
python3 db_manager.py
```

---

## Verify Tables

```bash
docker exec -it clickhouse-server \
clickhouse-client \
--query "SHOW TABLES"
```

---

# 🚀 Run Complete System

```bash
chmod +x main.py

python3 main.py
```

Expected:

```text
API server started

Workflow automation started

System monitor started

AIOps system is running
```

---

# 🌐 Test APIs

## Health

```bash
curl http://localhost:5000/health
```

---

## Metrics

```bash
curl http://localhost:5000/metrics
```

---

## Anomalies

```bash
curl http://localhost:5000/anomalies
```

---

## Prediction

```bash
curl -X POST http://localhost:5000/predict \
-H "Content-Type: application/json" \
-d '{"service":"web"}'
```

---

# 📊 Verify Data Flow

## ClickHouse Metrics

```bash
docker exec -it clickhouse-server clickhouse-client \
--query "SELECT service, count() FROM metrics GROUP BY service"
```

---

## Check Anomalies

```bash
docker exec -it clickhouse-server clickhouse-client \
--query "SELECT * FROM aggregated_metrics WHERE is_anomaly=1 LIMIT 10"
```

---

## Monitor Logs

```bash
tail -f logs/*.log
```

---

# 🛠 Troubleshooting

## ClickHouse Not Running

```bash
docker ps | grep clickhouse
```

Restart:

```bash
docker restart clickhouse-server
```

---

## Spark Memory Errors

Reduce batch size:

```python
batch_size = 50
```

Or increase Spark memory:

```python
.config("spark.driver.memory","4g")
```

---

## Port 5000 Already In Use

```bash
sudo lsof -i :5000
```

Kill process:

```bash
sudo kill -9 <PID>
```

---

## Dependency Problems

```bash
source venv/bin/activate

pip install -r requirements.txt
```

---

# 🎉 Expected Outcomes

After completing this lab you will have:

✅ Data Ingestion Pipeline

✅ Apache Spark Processing Engine

✅ ClickHouse Time-Series Storage

✅ REST API Platform

✅ Workflow Automation

✅ Monitoring & Alerting

✅ AI Prediction Engine

✅ End-to-End AIOps Architecture

---

# 📚 Key Takeaways

- Apache Spark enables scalable analytics.
- ClickHouse excels at time-series workloads.
- REST APIs provide easy integration.
- Workflow automation reduces operational overhead.
- AI models enable predictive operations.
- Monitoring and anomaly detection improve reliability.

---

# 🚀 Next Steps

- Integrate Prometheus
- Add Grafana Dashboards
- Deploy using Docker Compose
- Add Kafka Streaming
- Implement Kubernetes Deployment
- Add Advanced Forecasting Models
- Connect Slack / Email Alerting
- Integrate OpenTelemetry

---

<div align="center">

# 🏆 Congratulations!

You have successfully built a complete End-to-End AIOps Platform with:

⚡ Apache Spark  
🗄 ClickHouse  
🌐 Flask APIs  
🤖 Machine Learning  
🚨 Monitoring & Alerting  
🔄 Workflow Automation

Ready for Enterprise-Scale AIOps 🚀

</div>
