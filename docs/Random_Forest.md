# Random Forest Classifier

## Objective

The objective of this phase is to train a Random Forest Classifier to predict whether a customer is likely to default on a loan. The model combines multiple decision trees to improve predictive performance and reduce overfitting compared to a single Decision Tree.

---

## Why Random Forest?

Random Forest is an ensemble learning algorithm that builds multiple decision trees and combines their predictions.

### Advantages

- Reduces overfitting
- Handles non-linear relationships
- Provides feature importance
- Performs well on structured/tabular datasets
- More stable than a single Decision Tree

---

## Model Configuration

| Parameter | Value |
|-----------|-------|
| Number of Trees | 200 |
| Max Depth | 15 |
| Min Samples Split | 20 |
| Min Samples Leaf | 10 |
| Class Weight | Balanced |
| Random State | 42 |

---

## Model Performance

| Metric | Value |
|---------|-------|
| Accuracy | 79.25% |
| Precision | 19.03% |
| Recall | 48.22% |
| F1-Score | 27.29% |
| ROC-AUC | 73.23% |

---

## Confusion Matrix

| Actual / Predicted | Non-Default | Default |
|--------------------|------------:|--------:|
| Non-Default | 46,350 | 10,188 |
| Default | 2,571 | 2,394 |

### Interpretation

- Correctly identified 46,350 non-default customers.
- Correctly detected 2,394 default customers.
- Reduced false positives compared to previous models.
- Missed more default cases than Logistic Regression.

---

## Top Important Features

1. EXT_SOURCE_3
2. EXT_SOURCE_2
3. EXT_SOURCE_1
4. DAYS_BIRTH
5. DAYS_EMPLOYED
6. EMPLOYMENT_YEARS
7. DAYS_LAST_PHONE_CHANGE
8. AMT_GOODS_PRICE
9. AMT_CREDIT
10. AGE_YEARS
11. DAYS_ID_PUBLISH
12. AMT_ANNUITY
13. CREDIT_INCOME_RATIO
14. DAYS_REGISTRATION
15. ANNUITY_INCOME_RATIO

---

## Comparison

| Metric | Logistic Regression | Decision Tree | Random Forest |
|---------|--------------------:|--------------:|--------------:|
| Accuracy | 69.03% | 67.62% | **79.25%** |
| Precision | 16.14% | 14.84% | **19.03%** |
| Recall | **67.63%** | 63.52% | 48.22% |
| F1-Score | 26.07% | 24.06% | **27.29%** |
| ROC-AUC | **74.83%** | 70.01% | 73.23% |

---

## Conclusion

The Random Forest model outperformed the Decision Tree and achieved the highest Accuracy, Precision, and F1-score among the models tested so far. Although its Recall was lower than Logistic Regression, it provided a stronger overall balance between identifying defaulters and avoiding unnecessary loan rejections. It is a strong candidate for the final model, pending comparison with XGBoost.

