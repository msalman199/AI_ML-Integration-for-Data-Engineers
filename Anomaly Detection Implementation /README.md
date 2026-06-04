# 🤖 Anomaly Detection Implementation 

<p align="center">

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Scikit Learn](https://img.shields.io/badge/Scikit--Learn-ML-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data_Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-Scientific_Computing-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557C?style=for-the-badge)
![Machine Learning](https://img.shields.io/badge/Machine_Learning-Anomaly_Detection-success?style=for-the-badge)

</p>

---

# 📖 Overview

Anomaly Detection is a critical capability in modern AI, DevOps, Cybersecurity, and Monitoring systems. It helps identify unusual patterns, unexpected behavior, and abnormal events before they become major issues.

In this lab, you will build a complete anomaly detection pipeline using:

- 📊 Statistical Detection (Z-Score)
- 🤖 Machine Learning (Isolation Forest)
- 📈 Visualization & Evaluation
- 🔍 Real-Time Streaming Detection

---

# 🎯 Learning Objectives

By completing this lab, you will:

✅ Generate synthetic datasets with anomalies

✅ Implement statistical anomaly detection

✅ Train Isolation Forest models

✅ Evaluate model performance

✅ Visualize anomaly scores

✅ Perform real-time anomaly detection

---

# 📋 Prerequisites

Before starting this lab, ensure you have:

✅ Basic Python programming knowledge

✅ Understanding of arrays and dataframes

✅ Familiarity with Linux command line

✅ Basic statistics knowledge

- Mean
- Standard Deviation
- Outliers

✅ Experience running Python scripts

---

# 🛠️ Environment Setup

---

## 🔹 Step 1: Install Required Software

Update packages:

```bash
sudo apt update
```

Install Python:

```bash
sudo apt install -y python3 python3-pip python3-venv
```

Create project directory:

```bash
mkdir ~/anomaly-detection-lab
cd ~/anomaly-detection-lab
```

Create virtual environment:

```bash
python3 -m venv venv
```

Activate environment:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install numpy pandas scikit-learn matplotlib seaborn
```

---

## 🔹 Step 2: Verify Installation

```bash
python3 -c "
import sklearn
import pandas
import numpy
print('All packages installed successfully')
"
```

Expected:

```text
All packages installed successfully
```

---

# 🚀 Task 1: Load and Prepare Dataset

---

## 🔹 Step 1: Create Synthetic Dataset

Create file:

```bash
nano generate_data.py
```

### Features

The script should:

✅ Generate normal data

✅ Inject anomalies

✅ Create labels

✅ Export CSV dataset

---

### Complete Implementation Logic

#### Generate Normal Data

```python
np.random.seed(seed)

data = np.random.normal(
    loc=50,
    scale=10,
    size=n_samples
)
```

---

#### Inject Anomalies

```python
n_anomalies = int(len(data) * anomaly_ratio)

indices = np.random.choice(
    len(data),
    n_anomalies,
    replace=False
)

data[indices] = np.random.choice(
    [20, 80, 100],
    size=n_anomalies
)
```

---

#### Create DataFrame

Columns:

```python
value
timestamp
label
```

Labels:

```python
0 = Normal
1 = Anomaly
```

---

## 🔹 Step 2: Generate Dataset

Run:

```bash
python3 generate_data.py
```

Expected:

```text
Dataset created: 1000 samples
Anomalies: 50
```

---

## 🔹 Step 3: Explore Dataset

Create:

```bash
nano explore_data.py
```

Implement:

### Load CSV

```python
df = pd.read_csv(filepath)
```

Display:

```python
print(df.shape)

print(df.head())

print(df.describe())
```

---

### Create Visualization

Histogram:

```python
plt.hist(df['value'])
```

Highlight anomalies:

```python
plt.scatter(
    anomalies.index,
    anomalies['value'],
    color='red'
)
```

Save:

```python
plt.savefig('data_distribution.png')
```

---

Run:

```bash
python3 explore_data.py
```

Expected:

```text
data_distribution.png created
```

---

# 🤖 Task 2: Train Anomaly Detection Models

---

## 🔹 Step 1: Statistical Detection (Z-Score)

Create:

```bash
nano statistical_detector.py
```

---

### Fit Method

Calculate:

```python
self.mean = np.mean(X)

self.std = np.std(X)
```

---

### Predict Method

Calculate Z-Scores:

```python
z_scores = np.abs(
    (X - self.mean) / self.std
)
```

Prediction:

```python
(z_scores > self.threshold).astype(int)
```

---

### Score Method

```python
return np.abs(
    (X - self.mean) / self.std
)
```

---

## 🔹 Step 2: Isolation Forest Detector

Create:

```bash
nano ml_detector.py
```

Initialize model:

```python
IsolationForest(
    contamination=0.05,
    random_state=42
)
```

---

### Fit Model

```python
X = X.reshape(-1, 1)

self.model.fit(X)
```

---

### Predict

```python
predictions = self.model.predict(X)
```

Convert:

```python
np.where(
    predictions == -1,
    1,
    0
)
```

---

### Score

```python
self.model.decision_function(X)
```

---

## 🔹 Step 3: Train Models

Create:

```bash
nano train_models.py
```

Workflow:

```python
df = pd.read_csv('data.csv')

X = df['value'].values
```

Initialize:

```python
zscore = ZScoreDetector()

isolation = IsolationForestDetector()
```

Train:

```python
zscore.fit(X)

isolation.fit(X)
```

Save:

```python
pickle.dump(
    zscore,
    open('zscore_model.pkl','wb')
)
```

```python
pickle.dump(
    isolation,
    open('isolation_forest_model.pkl','wb')
)
```

---

Run:

```bash
python3 train_models.py
```

Expected:

```text
Models trained and saved successfully
```

---

# 📊 Task 3: Evaluate Model Performance

---

## 🔹 Step 1: Create Evaluation Script

Create:

```bash
nano evaluate.py
```

---

### Load Model

```python
pickle.load(
    open(model_path,'rb')
)
```

---

### Calculate Metrics

Precision:

```python
precision_score(
    y_true,
    y_pred
)
```

Recall:

```python
recall_score(
    y_true,
    y_pred
)
```

F1:

```python
f1_score(
    y_true,
    y_pred
)
```

---

### Confusion Matrix

```python
confusion_matrix(
    y_true,
    y_pred
)
```

---

## 🔹 Step 2: Run Evaluation

```bash
python3 evaluate.py
```

Expected:

```text
Model Comparison

ZScore
Precision: 0.82
Recall:    0.75
F1:        0.78

IsolationForest
Precision: 0.88
Recall:    0.80
F1:        0.84
```

---

# 📈 Task 4: Visualize Results

---

## 🔹 Step 1: Create Visualization Script

```bash
nano visualize_results.py
```

---

### Plot Anomaly Scores

Load:

```python
df = pd.read_csv('data.csv')
```

Score:

```python
model.score(X)
```

Plot:

```python
plt.scatter()
```

Highlight anomalies:

```python
color='red'
```

Save:

```python
plt.savefig(
    'anomaly_scores.png'
)
```

---

## 🔹 Step 2: Plot Confusion Matrices

Generate:

```python
confusion_matrix()
```

Display heatmaps:

```python
sns.heatmap()
```

Save:

```python
plt.savefig(
    'confusion_matrices.png'
)
```

---

Run:

```bash
python3 visualize_results.py
```

Expected:

```text
anomaly_scores.png
confusion_matrices.png
```

created successfully.

---

# ⚡ Task 5: Real-Time Detection

---

## 🔹 Step 1: Create Streaming Detector

Create:

```bash
nano test_streaming.py
```

---

### Load Model

```python
pickle.load(
    open(model_path,'rb')
)
```

---

### Generate Random Points

```python
np.random.normal(
    50,
    10,
    n_points
)
```

---

### Detect Anomalies

```python
prediction = model.predict(
    np.array([value])
)
```

---

### Print Results

```python
Point: 51.2 Normal

Point: 97.4 Anomaly

Point: 48.8 Normal
```

---

Run:

```bash
python3 test_streaming.py
```

---

# ✅ Verification

---

## Verify Files

```bash
ls -lh
```

Expected:

```text
data.csv

zscore_model.pkl

isolation_forest_model.pkl

data_distribution.png

anomaly_scores.png

confusion_matrices.png
```

---

## Verify Model Performance

```bash
python3 evaluate.py
```

Expected:

| Metric | Expected |
|----------|-----------|
| Precision | > 0.70 |
| Recall | > 0.60 |
| F1 Score | > 0.65 |

---

## Verify Visualizations

```bash
ls *.png
```

Expected:

```text
data_distribution.png

anomaly_scores.png

confusion_matrices.png
```

---

## Verify Streaming Detection

```bash
python3 test_streaming.py
```

Expected:

```text
Point: 49 Normal

Point: 110 Anomaly

Point: 52 Normal
```

---

# 📋 Verification Checklist

- [x] Python Environment Created
- [x] Dependencies Installed
- [x] Dataset Generated
- [x] Anomalies Injected
- [x] Z-Score Detector Implemented
- [x] Isolation Forest Implemented
- [x] Models Trained
- [x] Evaluation Completed
- [x] Visualizations Generated
- [x] Real-Time Detection Tested

---

# 🛠️ Troubleshooting

---

## ❌ ImportError

Activate virtual environment:

```bash
source venv/bin/activate
```

Reinstall:

```bash
pip install numpy pandas scikit-learn matplotlib seaborn
```

---

## ❌ Poor Model Performance

Verify:

- Anomaly ratio
- Contamination parameter
- Data generation logic

Recommended:

```python
contamination=0.05
```

---

## ❌ PNG Files Missing

Add:

```python
import matplotlib

matplotlib.use('Agg')
```

before pyplot imports.

---

## ❌ Memory Errors

Reduce dataset size:

```python
n_samples=500
```

or process data in batches.

---

# 🎓 Conclusion

Congratulations! You have successfully implemented an end-to-end anomaly detection pipeline.

You learned how to:

✅ Generate synthetic datasets

✅ Detect anomalies statistically

✅ Detect anomalies using machine learning

✅ Train and evaluate models

✅ Visualize anomaly scores

✅ Perform streaming anomaly detection

---

# 💡 Key Takeaways

### 📊 Z-Score Detection

Works best for normally distributed datasets.

---

### 🤖 Isolation Forest

Excellent for non-linear and complex anomaly patterns.

---

### 📈 Evaluation Matters

Precision, Recall, and F1 Score are essential metrics.

---

### ⚡ Real-Time Detection

Streaming anomaly detection is critical for:

- Monitoring Systems
- Fraud Detection
- Cybersecurity
- DevOps Observability

---

# 🌍 Real-World Applications

Anomaly Detection is used in:

✅ AIOps Platforms

✅ Fraud Detection Systems

✅ SIEM & Cybersecurity

✅ IoT Monitoring

✅ Predictive Maintenance

✅ Financial Risk Management

✅ Cloud Infrastructure Monitoring

---

# 🚀 Next Steps

### 🔹 One-Class SVM

Experiment with additional ML methods.

### 🔹 Autoencoders

Apply Deep Learning anomaly detection.

### 🔹 Multivariate Data

Detect anomalies across multiple features.

### 🔹 Streaming Analytics

Use Kafka + Spark Streaming.

### 🔹 Production Monitoring

Integrate with:

- Prometheus
- Grafana
- ELK Stack
- OpenTelemetry

---

# 📚 Additional Resources

### Scikit-Learn Anomaly Detection

https://scikit-learn.org/stable/modules/outlier_detection.html

### Isolation Forest Paper

Liu et al. (2008)

### Statistical Process Control

Control Charts & Outlier Detection Techniques

---

# 🏆 Lab Completed Successfully

```text
✔ Environment Setup Complete
✔ Dataset Generated
✔ Anomalies Injected
✔ Statistical Model Built
✔ Isolation Forest Trained
✔ Models Evaluated
✔ Visualizations Created
✔ Streaming Detection Tested
✔ Performance Verified
```

🎉 Congratulations! You now have practical experience building anomaly detection systems used in modern AI, DevOps, cybersecurity, and observability platforms.
