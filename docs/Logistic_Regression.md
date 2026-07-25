# Logistic Regression Classifier

## Objective

The objective of this phase is to build a Logistic Regression model as the baseline machine learning model for predicting whether a customer is likely to default on a loan. This model provides a simple, interpretable benchmark that will be compared with more advanced machine learning algorithms.

---

## Why Logistic Regression?

Logistic Regression is one of the most widely used algorithms for binary classification problems such as credit risk prediction.

### Advantages

- Simple and easy to interpret
- Fast to train on large datasets
- Produces probability scores
- Works well as a baseline model
- Easy to compare with advanced models

---

## Data Preprocessing

Before training the model, the following preprocessing steps were performed:

- Removed unnecessary columns such as `SK_ID_CURR`
- Handled missing values
- Applied One-Hot Encoding to categorical variables
- Created new features:
  - AGE_YEARS
  - EMPLOYMENT_YEARS
  - CREDIT_INCOME_RATIO
  - ANNUITY_INCOME_RATIO
- Split the dataset into 80% training and 20% testing sets using stratified sampling.
- Applied **StandardScaler** to scale the numerical features.
- Used `class_weight='balanced'` to handle the class imbalance.

---

## Model Configuration

| Parameter | Value |
|-----------|-------|
| Algorithm | Logistic Regression |
| Solver | lbfgs |
| Max Iterations | 1000 |
| Class Weight | Balanced |
| Random State | 42 |

---

## Model Performance

| Metric | Value |
|---------|-------|
| Accuracy | **69.03%** |
| Precision | **16.14%** |
| Recall | **67.63%** |
| F1-Score | **26.07%** |
| ROC-AUC Score | **74.83%** |

---

## Classification Report

| Class | Precision | Recall | F1-Score | Support |
|-------|----------:|-------:|---------:|--------:|
| Non-Default (0) | 0.96 | 0.69 | 0.80 | 56,538 |
| Default (1) | 0.16 | 0.68 | 0.26 | 4,965 |

Overall Accuracy: **69.03%**

---

## Confusion Matrix

| Actual / Predicted | Non-Default | Default |
|--------------------|------------:|--------:|
| Non-Default | 39,095 | 17,443 |
| Default | 1,607 | 3,358 |

### Interpretation

- **True Negatives (39,095):** Customers correctly classified as non-defaulters.
- **True Positives (3,358):** Customers correctly classified as defaulters.
- **False Positives (17,443):** Customers incorrectly predicted as defaulters even though they would repay the loan.
- **False Negatives (1,607):** Customers incorrectly predicted as safe but actually defaulted.

---

## Business Interpretation

From a business perspective:

- The model successfully identified approximately **68% of customers who were likely to default**, helping the bank reduce financial risk.
- Due to the imbalanced nature of the dataset, the model also classified many good customers as risky (false positives).
- Although this could lead to some unnecessary loan rejections, the model prioritizes identifying risky customers, which is often preferred in credit risk management.

---

## Advantages of This Model

- Easy to understand and explain.
- Produces probability scores for each customer.
- Handles imbalanced data using `class_weight='balanced'`.
- Serves as a strong baseline model for comparison with more advanced algorithms.

---

## Limitations

- Assumes a mostly linear relationship between features and the target variable.
- Produced a relatively low precision due to the large number of false positives.
- May not capture complex patterns present in customer financial data.

---

## Conclusion

The Logistic Regression model achieved a **ROC-AUC score of 74.83%**, demonstrating a good ability to distinguish between customers who are likely to default and those who are not.

Although the model produced a lower precision because of the imbalanced dataset, it achieved a high recall, making it effective at identifying risky customers. This model serves as the baseline for comparison with Decision Tree, Random Forest, and XGBoost models in the subsequent stages of the project.

---
