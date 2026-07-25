# Decision Tree Classifier

## Objective

The objective of this step is to build a Decision Tree Classifier to predict whether a customer is likely to default on a loan. The model is compared with the Logistic Regression model to determine whether it provides better predictive performance for credit risk prediction.

---

## Why Decision Tree?

A Decision Tree is a supervised machine learning algorithm used for classification problems. It learns decision rules from the training data by splitting it into smaller groups based on feature values.

### Advantages

- Captures non-linear relationships
- Easy to understand and visualize
- Provides feature importance
- Does not require feature scaling
- Can model complex decision boundaries

---

## Model Hyperparameters

| Parameter | Value |
|-----------|-------|
| Criterion | Gini |
| Max Depth | 10 |
| Min Samples Split | 20 |
| Min Samples Leaf | 10 |
| Class Weight | Balanced |
| Random State | 42 |

These parameters were chosen to reduce overfitting while improving the model's ability to generalize on unseen data.

---

## Model Performance

| Metric | Value |
|---------|-------|
| Accuracy | 67.62% |
| Precision | 14.84% |
| Recall | 63.52% |
| F1-Score | 24.06% |
| ROC-AUC Score | 70.01% |

---

## Classification Report

| Class | Precision | Recall | F1-Score | Support |
|-------|----------:|-------:|---------:|--------:|
| Non-Default (0) | 0.96 | 0.68 | 0.79 | 56,538 |
| Default (1) | 0.15 | 0.64 | 0.24 | 4,965 |

Overall Accuracy: **67.62%**

---

## Confusion Matrix

| Actual / Predicted | Non-Default | Default |
|--------------------|------------:|--------:|
| Non-Default | 38,435 | 18,103 |
| Default | 1,811 | 3,154 |

### Interpretation

- **True Negatives (38,435):** Customers correctly classified as non-defaulters.
- **True Positives (3,154):** Customers correctly classified as defaulters.
- **False Positives (18,103):** Customers incorrectly predicted as defaulters even though they would repay the loan.
- **False Negatives (1,811):** Customers incorrectly predicted as safe but actually defaulted.

---

## Top Important Features

The Decision Tree identified the following features as the most important for predicting loan default:

1. EXT_SOURCE_3
2. EXT_SOURCE_2
3. EXT_SOURCE_1
4. EMPLOYMENT_YEARS
5. AMT_ANNUITY
6. AMT_CREDIT
7. CREDIT_INCOME_RATIO
8. DAYS_BIRTH
9. ANNUITY_INCOME_RATIO
10. AMT_GOODS_PRICE
11. DAYS_REGISTRATION
12. DAYS_EMPLOYED
13. DAYS_LAST_PHONE_CHANGE
14. DAYS_ID_PUBLISH
15. NAME_EDUCATION_TYPE_Secondary / secondary special

These features contributed the most to the model's decision-making process.

---

## Comparison with Logistic Regression

| Metric | Logistic Regression | Decision Tree |
|---------|--------------------:|--------------:|
| Accuracy | **69.03%** | 67.62% |
| Precision | **16.14%** | 14.84% |
| Recall | **67.63%** | 63.52% |
| F1-Score | **26.07%** | 24.06% |
| ROC-AUC | **74.83%** | 70.01% |

### Observation

The Decision Tree model performed slightly worse than the Logistic Regression model across all evaluation metrics. Although it successfully captured non-linear relationships and provided feature importance, its predictive performance was lower than the baseline model.

---

## Business Interpretation

From a business perspective:

- The model correctly identified many customers who are likely to repay their loans.
- It also detected a significant number of customers who may default.
- However, it generated many false positives, meaning some reliable customers could be wrongly classified as high risk.
- This could lead to unnecessary loan rejections and reduced customer satisfaction.

---

## Conclusion

The Decision Tree model demonstrated the ability to learn complex decision rules and identify the most influential features affecting loan default. However, its overall predictive performance was lower than the Logistic Regression model.

Therefore, the Decision Tree was **not selected as the final model**. It will be retained for comparison purposes, while more advanced ensemble algorithms such as **Random Forest** and **XGBoost** will be evaluated in the next stages of the project.

---

