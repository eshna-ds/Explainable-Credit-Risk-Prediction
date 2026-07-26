# XGBoost Classifier

## Objective

Train an XGBoost model to predict customer loan defaults and compare its performance with Logistic Regression, Decision Tree, and Random Forest models.

---

## Why XGBoost?

XGBoost is a Gradient Boosting algorithm that builds decision trees sequentially. Each new tree attempts to correct the mistakes made by previous trees, resulting in strong predictive performance.

### Advantages

- Excellent performance on structured datasets
- Handles complex relationships
- Reduces overfitting
- Handles imbalanced datasets using scale_pos_weight
- Provides feature importance

---

## Model Parameters

| Parameter | Value |
|-----------|-------|
| Number of Trees | 300 |
| Max Depth | 6 |
| Learning Rate | 0.05 |
| Subsample | 0.8 |
| Column Sample by Tree | 0.8 |
| Scale Positive Weight | Calculated from training data |
| Random State | 42 |

---

## Model Performance

| Metric | Value |
|---------|-------|
| Accuracy | 72.33% |
| Precision | 17.52% |
| Recall | 65.48% |
| F1-Score | 27.65% |
| ROC-AUC | 75.95% |

---

## Confusion Matrix

| Actual / Predicted | Non-Default | Default |
|--------------------|------------:|--------:|
| Non-Default | 41,237 | 15,301 |
| Default | 1,714 | 3,251 |

---

## Top Important Features

1. EXT_SOURCE_2
2. EXT_SOURCE_3
3. NAME_EDUCATION_TYPE_Higher education
4. EMPLOYMENT_YEARS
5. CODE_GENDER_M
6. EXT_SOURCE_1
7. NAME_EDUCATION_TYPE_Secondary / secondary special
8. FLAG_DOCUMENT_3
9. FLAG_OWN_CAR_Y
10. NAME_CONTRACT_TYPE_Revolving loans
11. AMT_GOODS_PRICE
12. NAME_FAMILY_STATUS_Married
13. DEF_60_CNT_SOCIAL_CIRCLE
14. OCCUPATION_TYPE_Core staff
15. REGION_RATING_CLIENT_W_CITY

---

## Conclusion

Among all evaluated models, XGBoost achieved the highest ROC-AUC score and F1-score, demonstrating the best balance between identifying defaulters and minimizing classification errors. Based on these results, XGBoost was selected as the final predictive model for the Explainable Credit Risk Prediction project.

