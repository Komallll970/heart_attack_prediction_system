<div align="center">

# ❤️ Heart Attack Prediction System

### Machine Learning-Based Heart Attack Risk Prediction

<p>
  <b>Predicting Heart Attack Risk Using Clinical & Health-Related Parameters</b>
</p>

<p>
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white">
  <img src="https://img.shields.io/badge/SVC-Classification-6A5ACD?style=for-the-badge">
  <img src="https://img.shields.io/badge/Healthcare-Machine%20Learning-2E8B57?style=for-the-badge">
</p>

<p>
  <i>
    An end-to-end Machine Learning classification project that predicts
    heart attack risk using demographic, clinical, and health-related parameters.
  </i>
</p>

</div>

<hr>

## 📌 Overview

The <b>Heart Attack Prediction System</b> is a Machine Learning-based classification project developed to predict whether an individual is at risk of experiencing a heart attack based on various health and clinical parameters.

The model uses features such as:

<ul>
  <li>Age</li>
  <li>Cholesterol level</li>
  <li>Blood pressure</li>
  <li>Heart rate</li>
  <li>Other health-related parameters</li>
</ul>

A <b>Support Vector Classifier (SVC)</b> was trained to identify patterns in the input health data and classify individuals according to the target outcome.

The model achieved <b>98.54% test accuracy</b> and a <b>98.54% F1-score</b> on the evaluated test dataset.

> ⚠️ <b>Disclaimer:</b> This project is intended for educational and Machine Learning demonstration purposes only. It is not a medical diagnostic tool and should not be used to make healthcare decisions.

---

## 🎯 Project Objectives

<ul>
  <li>Develop a Machine Learning model for heart attack risk prediction.</li>
  <li>Analyze relationships between health parameters and the target outcome.</li>
  <li>Prepare clinical and demographic features for Machine Learning.</li>
  <li>Train an SVC classification model.</li>
  <li>Evaluate model performance on unseen test data.</li>
  <li>Measure performance using accuracy and F1-score.</li>
</ul>

---

## 🧠 Machine Learning Approach

<table>
<tr>
<th>Component</th>
<th>Technique</th>
</tr>

<tr>
<td><b>Problem Type</b></td>
<td>Binary Classification</td>
</tr>

<tr>
<td><b>Algorithm</b></td>
<td>Support Vector Classifier (SVC)</td>
</tr>

<tr>
<td><b>Input</b></td>
<td>Clinical & Health Parameters</td>
</tr>

<tr>
<td><b>Output</b></td>
<td>Heart Attack Risk Prediction</td>
</tr>

<tr>
<td><b>Evaluation Metrics</b></td>
<td>Accuracy, F1-Score</td>
</tr>
</table>

---

## 📊 Model Performance

The trained SVC model demonstrated strong performance on the test dataset.

<table>
<tr>
<th>Evaluation Metric</th>
<th>Score</th>
</tr>

<tr>
<td><b>Test Accuracy</b></td>
<td><b>98.54%</b></td>
</tr>

<tr>
<td><b>Test F1-Score</b></td>
<td><b>98.54%</b></td>
</tr>
</table>

<div align="center">

### 📈 Test Performance

```text
┌────────────────────────────────┐
│      HEART ATTACK MODEL        │
├────────────────────────────────┤
│                                │
│  Accuracy     →    98.54%      │
│  F1-Score     →    98.54%      │
│                                │
└────────────────────────────────┘
```

</div>

---

## 🔄 Project Workflow

<div align="center">

```text
                ┌────────────────────────┐
                │   Healthcare Dataset   │
                └────────────┬───────────┘
                             │
                             ▼
                ┌────────────────────────┐
                │   Data Understanding   │
                │    & EDA               │
                └────────────┬───────────┘
                             │
                             ▼
                ┌────────────────────────┐
                │  Data Preprocessing    │
                │                        │
                │ • Missing Values       │
                │ • Feature Preparation  │
                │ • Data Transformation  │
                └────────────┬───────────┘
                             │
                             ▼
                ┌────────────────────────┐
                │    Train-Test Split    │
                └────────────┬───────────┘
                             │
                             ▼
                ┌────────────────────────┐
                │      SVC Model         │
                │      Training          │
                └────────────┬───────────┘
                             │
                             ▼
                ┌────────────────────────┐
                │    Model Prediction    │
                └────────────┬───────────┘
                             │
                             ▼
                ┌────────────────────────┐
                │   Model Evaluation     │
                │                        │
                │ Accuracy + F1-Score    │
                └────────────┬───────────┘
                             │
                             ▼
                ┌────────────────────────┐
                │ Heart Attack Risk      │
                │      Prediction        │
                └────────────────────────┘
```

</div>

---

## 🔬 Data & Feature Preparation

The dataset contains health-related variables that can be used to identify patterns associated with the target outcome.

Example input features include:

<table>
<tr>
<th>Feature Category</th>
<th>Examples</th>
</tr>

<tr>
<td><b>Demographic</b></td>
<td>Age</td>
</tr>

<tr>
<td><b>Cardiovascular</b></td>
<td>Blood Pressure, Heart Rate</td>
</tr>

<tr>
<td><b>Blood Parameters</b></td>
<td>Cholesterol</td>
</tr>

<tr>
<td><b>Other Health Parameters</b></td>
<td>Additional clinical variables available in the dataset</td>
</tr>
</table>

The data preparation workflow includes examining the dataset, preparing the features, splitting the data into training and testing sets, and preparing the inputs for the SVC model.

---

## 🤖 Why SVC?

<b>Support Vector Classifier (SVC)</b> was selected as the classification algorithm for this project.

SVC works by finding a decision boundary that separates different classes while attempting to maximize the margin between them.

For this project, the model learns patterns between the available health-related parameters and the target outcome.

The approach is particularly useful for demonstrating how supervised Machine Learning can be applied to binary classification problems involving multiple numerical and categorical features.

---

## 📈 Model Evaluation

The model was evaluated on a separate test dataset that was not used during model training.

### Accuracy

Accuracy measures the proportion of correctly classified observations:

```text
Accuracy = Correct Predictions / Total Predictions
```

The model achieved:

```text
Test Accuracy → 98.54%
```

### F1-Score

The F1-score provides a balance between precision and recall and is useful for evaluating classification performance.

The model achieved:

```text
Test F1-Score → 98.54%
```

---

## 📊 Confusion Matrix

A confusion matrix can be used to analyze the classification results in more detail by showing:

```text
                    Predicted
                 Negative   Positive
              ┌───────────┬───────────┐
Actual Negative│    TN     │    FP     │
              ├───────────┼───────────┤
Actual Positive│    FN     │    TP     │
              └───────────┴───────────┘
```

This provides insight into the types of correct and incorrect predictions made by the model.

---

## 🛠️ Technologies & Libraries

<table>
<tr>
<td><b>Programming Language</b></td>
<td>Python</td>
</tr>

<tr>
<td><b>Machine Learning</b></td>
<td>Scikit-learn</td>
</tr>

<tr>
<td><b>Classification Algorithm</b></td>
<td>Support Vector Classifier (SVC)</td>
</tr>

<tr>
<td><b>Data Manipulation</b></td>
<td>Pandas, NumPy</td>
</tr>

<tr>
<td><b>Visualization</b></td>
<td>Matplotlib, Seaborn</td>
</tr>

<tr>
<td><b>Development Environment</b></td>
<td>Jupyter Notebook / Google Colab / VS Code</td>
</tr>
</table>

---

## 📂 Project Structure

```text
Heart-Attack-Prediction/
│
├── 📁 dataset/
│   └── heart_attack_dataset.csv
│
├── 📁 notebooks/
│   └── heart_attack_prediction.ipynb
│
├── 📁 models/
│   └── heart_attack_svc_model.pkl
│
├── 📁 images/
│   ├── eda.png
│   ├── confusion_matrix.png
│   └── model_performance.png
│
├── requirements.txt
├── README.md
└── LICENSE
```

<i>Update the structure according to the actual files and folders in your repository.</i>

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/Heart-Attack-Prediction.git
cd Heart-Attack-Prediction
```

### 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
```

### 3️⃣ Activate the Environment

<b>Windows:</b>

```bash
venv\Scripts\activate
```

<b>macOS / Linux:</b>

```bash
source venv/bin/activate
```

### 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run

If the project is implemented using Jupyter Notebook:

```bash
jupyter notebook
```

Open:

```text
notebooks/heart_attack_prediction.ipynb
```

Run the notebook cells sequentially.

The complete workflow follows:

```text
Load Dataset
     ↓
Explore Data
     ↓
Preprocess Features
     ↓
Train-Test Split
     ↓
Train SVC Model
     ↓
Generate Predictions
     ↓
Evaluate Model
     ↓
Heart Attack Risk Prediction
```

---

## 💡 Key Features

<table>
<tr>
<td>❤️</td>
<td><b>Risk Prediction</b></td>
<td>Predicts the target heart attack risk outcome from health-related parameters.</td>
</tr>

<tr>
<td>🩺</td>
<td><b>Health Parameters</b></td>
<td>Uses variables such as age, cholesterol, blood pressure, and other available health features.</td>
</tr>

<tr>
<td>🤖</td>
<td><b>SVC Classification</b></td>
<td>Uses Support Vector Classification for supervised prediction.</td>
</tr>

<tr>
<td>📊</td>
<td><b>Model Evaluation</b></td>
<td>Evaluates performance using test accuracy and F1-score.</td>
</tr>

<tr>
<td>📈</td>
<td><b>Performance Analysis</b></td>
<td>Supports further analysis using confusion matrix and classification metrics.</td>
</tr>
</table>

---

## 🚀 Future Improvements

<ul>
  <li>Develop an interactive Streamlit web application.</li>
  <li>Deploy the model using Flask or FastAPI.</li>
  <li>Compare SVC with Random Forest, Logistic Regression, XGBoost, and other classifiers.</li>
  <li>Add cross-validation for more robust model evaluation.</li>
  <li>Perform systematic hyperparameter tuning.</li>
  <li>Implement explainable AI techniques such as SHAP.</li>
  <li>Add probability-based predictions where appropriate.</li>
  <li>Improve model monitoring and validation using external datasets.</li>
</ul>

---

## 📚 Key Learning Outcomes

Through this project, the following concepts were implemented:

<ul>
  <li>Data preprocessing</li>
  <li>Exploratory Data Analysis</li>
  <li>Feature preparation</li>
  <li>Supervised Machine Learning</li>
  <li>Binary classification</li>
  <li>Support Vector Machine / SVC</li>
  <li>Train-test splitting</li>
  <li>Model evaluation</li>
  <li>Confusion matrix analysis</li>
  <li>Accuracy and F1-score interpretation</li>
</ul>

---

## ⚠️ Medical Disclaimer

<div align="center">

<b>Important:</b>

This project is developed strictly for educational, portfolio, and Machine Learning demonstration purposes.

It is <b>not a medical diagnostic system</b> and should not be used to diagnose, treat, or make medical decisions about any individual.

Always consult a qualified healthcare professional for medical advice, diagnosis, and treatment.

</div>

---

## 👩‍💻 Author

<div align="center">

### Komal Verma

<b>Data Science | Machine Learning | Python</b>

<p>
  <i>
    Building practical Machine Learning solutions for real-world problems.
  </i>
</p>

</div>

---

## ⭐ Project Highlights

```text
❤️ HEART ATTACK PREDICTION SYSTEM
│
├── 🩺 Health & Clinical Feature Analysis
│
├── 🤖 SVC Classification
│
├── 📊 Test Accuracy
│   └── 98.54%
│
├── 📈 Test F1-Score
│   └── 98.54%
│
└── 🧠 End-to-End Machine Learning Workflow
    ├── Data Preparation
    ├── Model Training
    ├── Prediction
    └── Evaluation
```

<div align="center">

<b>⭐ If you found this project useful, consider giving the repository a star!</b>

<br><br>

<i>Built with Python & Machine Learning ❤️🤖</i>

</div>
