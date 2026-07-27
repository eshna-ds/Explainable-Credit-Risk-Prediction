# 📌 Project Overview

Financial institutions use machine learning models to evaluate loan applications. While these models provide accurate predictions, they often work as **black boxes**, making it difficult to explain why a customer's loan was approved or rejected.

This project develops an **Explainable Credit Risk Prediction System** that not only predicts whether a customer is likely to default on a loan but also explains **why** the prediction was made using **SHAP (SHapley Additive exPlanations)**.

The project demonstrates an end-to-end Machine Learning workflow, including data preprocessing, feature engineering, model comparison, explainable AI, and deployment through Streamlit.

---

# 🎯 Business Problem

Banks receive thousands of loan applications every day.

Approving loans for risky customers can result in significant financial losses, while rejecting reliable customers can reduce business opportunities.

Traditional machine learning models often provide only predictions without explanations.

### Example

Customer:

> "Why was my loan rejected?"

Traditional ML Model:

> "High Risk"

Explainable AI Model:

> "Your loan was rejected mainly because of:
>
> - Low external credit score
> - High credit amount
> - Low annual income
> - Short employment history"

This makes the decision transparent and helps banks comply with explainability requirements.

---

# 💡 Solution

The project predicts whether a customer is likely to default on a loan using **XGBoost** and explains every prediction using **SHAP**.

### Workflow

```
Customer Information
        │
        ▼
Data Preprocessing
        │
        ▼
Feature Engineering
        │
        ▼
Train ML Models
        │
        ▼
Best Model (XGBoost)
        │
        ▼
Predict Loan Risk
        │
        ▼
SHAP Explainability
        │
        ▼
Interactive Streamlit Dashboard
```

---

# 📂 Dataset

**Dataset Name**

Home Credit Default Risk Dataset

**Source**

Kaggle

https://www.kaggle.com/competitions/home-credit-default-risk

---

## Dataset Information

| Property | Value |
|-----------|--------|
| Records | 307,511 |
| Features | 122 |
| Target | TARGET |
| Missing Values | Yes |
| Numerical Features | 65 |
| Categorical Features | 16 |

### Target Variable

| Value | Meaning |
|--------|---------|
| 0 | Loan Repaid |
| 1 | Loan Default |

---

# ⚙️ Project Workflow

## 1. Data Collection

- Home Credit Default Risk Dataset
- Customer financial information
- Credit history
- Demographic information

---

## 2. Data Preprocessing

- Missing value treatment
- Categorical encoding
- Feature selection
- Data cleaning

---

## 3. Feature Engineering

Created additional features including:

- AGE_YEARS
- EMPLOYMENT_YEARS
- CREDIT_INCOME_RATIO
- ANNUITY_INCOME_RATIO

---

## 4. Machine Learning Models

Three machine learning models were trained and compared.

| Model | Purpose |
|--------|----------|
| Logistic Regression | Baseline Model |
| Random Forest | Ensemble Learning |
| XGBoost | Final Model |

---

# 📈 Model Evaluation

The models were evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC Score

### Final Model Performance (XGBoost)

| Metric | Score |
|---------|-------|
| Accuracy | 72% |
| Precision | 18% |
| Recall | 65% |
| ROC-AUC | 0.76 |

> **Note:** In credit risk prediction, recall is particularly important because identifying risky customers helps reduce financial losses for the bank.

---

# 🤖 Explainable AI (SHAP)

Instead of providing only predictions, the model explains the factors that contributed to each decision.

The project includes:

- SHAP Waterfall Plot
- SHAP Feature Importance
- Individual Prediction Explanation

This improves transparency and helps users understand model decisions.

---

# 🖥️ Streamlit Dashboard

The project includes an interactive web application built using Streamlit.

### Features

- Customer Information Input
- Loan Risk Prediction
- Default Probability
- SHAP Explainability
- Feature Importance
- Download Prediction Report

---

# 📁 Project Structure

```
Explainable-Credit-Risk-Prediction/

│
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── data/
│
├── models/
│   ├── xgboost.pkl
│   └── feature_columns.pkl
│
├── notebooks/
│
├── reports/
│
├── docs/
│
├── images/
│
└── src/
```

---

# 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- XGBoost
- SHAP
- Streamlit
- Joblib

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Explainable-Credit-Risk-Prediction.git
```

Move into the project directory

```bash
cd Explainable-Credit-Risk-Prediction
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Streamlit app

```bash
streamlit run app.py
```

---

# 📊 Results

The XGBoost model demonstrated the best performance among the evaluated algorithms.

The application successfully:

- Predicts customer loan default risk
- Provides prediction probability
- Explains predictions using SHAP
- Displays feature importance
- Offers an interactive user interface

---

# 🔮 Future Improvements

- Hyperparameter Optimization
- Cross Validation
- Model Monitoring
- Cloud Deployment
- Real-Time Prediction API
- Loan Approval Recommendation System
- Fairness and Bias Analysis
- Automated Data Pipeline

---

# 📚 Learning Outcomes

Through this project, I gained practical experience in:

- Data Cleaning
- Feature Engineering
- Machine Learning
- Model Evaluation
- Explainable AI
- XGBoost
- SHAP
- Streamlit Deployment
- GitHub Project Management

---

# 👩‍💻 Author

**Eshna Jain**

B.Tech Computer Science Engineering (AI & DS)

Passionate about Machine Learning, Data Science, and Explainable AI.

---

# ⭐ If you found this project useful, consider giving it a star!