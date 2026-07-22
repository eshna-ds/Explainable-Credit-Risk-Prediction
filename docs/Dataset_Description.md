# Dataset Description

## Dataset Name

Home Credit Default Risk Dataset

---

## Dataset Source

* **Platform:** Kaggle
* **Dataset:** Home Credit Default Risk
* **Provider:** Home Credit Group

---

## Purpose

The Home Credit Default Risk dataset contains historical loan application data collected by Home Credit Group. The purpose of this dataset is to help build a machine learning model that predicts whether a customer will have difficulty repaying a loan.

Many people with limited or no credit history find it difficult to obtain loans. Home Credit aims to use alternative customer information to make fair lending decisions while reducing the risk of loan defaults.

---

## Problem Type

Binary Classification

The machine learning model predicts whether a customer is likely to repay the loan or default on it.

---

## Target Variable

**TARGET**

* **0** = Customer successfully repaid the loan (Low Credit Risk)
* **1** = Customer had payment difficulties or defaulted on the loan (High Credit Risk)

---

## Dataset Size

The project uses the **application_train.csv** file.

* Approximately **307,511** customer records
* **122** features (customer attributes)

---

## Important Features

Some of the important features used in this project include:

| Feature             | Description                                                          |
| ------------------- | -------------------------------------------------------------------- |
| TARGET              | Loan repayment status (Target Variable)                              |
| AMT_INCOME_TOTAL    | Customer's annual income                                             |
| AMT_CREDIT          | Total loan amount requested                                          |
| AMT_ANNUITY         | Loan installment amount                                              |
| AMT_GOODS_PRICE     | Price of the purchased goods                                         |
| DAYS_BIRTH          | Customer's age (stored as negative days before the application date) |
| DAYS_EMPLOYED       | Number of days the customer has been employed                        |
| NAME_EDUCATION_TYPE | Education level                                                      |
| NAME_FAMILY_STATUS  | Marital status                                                       |
| NAME_INCOME_TYPE    | Type of income (Working, Pensioner, etc.)                            |
| OCCUPATION_TYPE     | Customer's occupation                                                |
| CODE_GENDER         | Customer's gender                                                    |
| CNT_CHILDREN        | Number of children                                                   |
| CNT_FAM_MEMBERS     | Number of family members                                             |
| FLAG_OWN_CAR        | Whether the customer owns a car                                      |
| FLAG_OWN_REALTY     | Whether the customer owns a house or property                        |

---

## Why This Dataset?

This dataset was chosen because:

* It represents a real-world banking loan approval problem.
* It is widely used in data science competitions and research.
* It contains both numerical and categorical features.
* It is suitable for classification problems.
* It allows the use of Explainable AI (SHAP) to explain model predictions.
* It closely matches real credit risk assessment used by financial institutions.

---

## Project Objective

The objective of this project is to build a machine learning model that predicts whether a customer is likely to default on a loan. In addition, SHAP (SHapley Additive exPlanations) will be used to explain every prediction by identifying the features that most influenced the model's decision. This makes the model more transparent, trustworthy, and easier to understand for both banks and customers.

---

## Expected Outcome

After completing this project, the system will:

* Predict whether a customer is a low-risk or high-risk borrower.
* Explain why a loan application is classified as risky or safe.
* Display the most important features affecting each prediction using SHAP.
* Help improve transparency and trust in AI-based credit risk assessment.
