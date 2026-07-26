# SHAP Explainability

## Objective

The objective of this phase is to explain the predictions made by the XGBoost model. Instead of treating the model as a black box, SHAP (SHapley Additive exPlanations) helps identify how each feature contributes to the prediction for every customer.

This improves model transparency and helps financial institutions justify automated loan approval or rejection decisions.

---

# What is SHAP?

SHAP (SHapley Additive exPlanations) is an Explainable Artificial Intelligence (XAI) technique based on cooperative game theory.

It explains:

- Why a prediction was made
- Which features increased the predicted risk
- Which features reduced the predicted risk
- The contribution of every feature to an individual prediction

Unlike traditional feature importance, SHAP provides both **global explanations** (overall model behavior) and **local explanations** (individual customer predictions).

---

# Why SHAP?

Financial institutions cannot rely solely on black-box models because regulations often require loan decisions to be explainable.

Using SHAP allows the bank to:

- Explain every loan decision
- Increase customer trust
- Improve regulatory compliance
- Understand model behavior
- Detect potential bias in predictions

---

# SHAP Visualizations

The following SHAP visualizations were generated:

- SHAP Summary Plot (Beeswarm Plot)
- SHAP Feature Importance Bar Plot
- SHAP Waterfall Plot
- SHAP Dependence Plot

---

# SHAP Summary Plot Analysis

The SHAP Summary Plot shows the overall impact of each feature on the model's predictions across all customers.

## Top Features

1. EXT_SOURCE_3
2. EXT_SOURCE_2
3. AMT_GOODS_PRICE
4. EXT_SOURCE_1
5. CODE_GENDER_M
6. AMT_CREDIT
7. EMPLOYMENT_YEARS
8. FLAG_OWN_CAR_Y
9. AMT_ANNUITY
10. NAME_EDUCATION_TYPE_Higher education

## Observation

- EXT_SOURCE_3 and EXT_SOURCE_2 are the most influential features.
- Customers with lower external credit scores tend to have a higher predicted default risk.
- Customers with higher external credit scores tend to have a lower predicted default risk.
- Loan amount and employment-related features also significantly influence the prediction.

---

# SHAP Feature Importance Plot

The SHAP Feature Importance Plot ranks the features according to their average impact on model predictions.

## Most Important Features

- EXT_SOURCE_3
- EXT_SOURCE_2
- AMT_GOODS_PRICE
- EXT_SOURCE_1
- CODE_GENDER_M
- AMT_CREDIT
- EMPLOYMENT_YEARS

## Observation

The model relies primarily on external credit score features, followed by loan amount and employment-related information.

---

# SHAP Waterfall Plot

The Waterfall Plot explains the prediction for a single customer.

## Model Prediction

Prediction Output (f(x)) = **-0.857**

The customer is predicted to be **Low Risk**.

## Features That Reduced Risk

- AMT_GOODS_PRICE
- EXT_SOURCE_2
- NAME_EDUCATION_TYPE_Higher education
- AMT_REQ_CREDIT_BUREAU_QRT
- FLAG_OWN_CAR_Y
- FLAG_DOCUMENT_3

## Features That Increased Risk

- CODE_GENDER_M
- DAYS_EMPLOYED
- EMPLOYMENT_YEARS

## Interpretation

Although a few employment-related features slightly increased the predicted risk, the customer's strong external credit score, higher education level, and other favorable characteristics reduced the overall risk. As a result, the model classified the customer as low risk.

---

# SHAP Dependence Plot

The Dependence Plot illustrates how EXT_SOURCE_2 influences the prediction.

## Observation

- As EXT_SOURCE_2 increases, the SHAP value generally decreases.
- Higher EXT_SOURCE_2 values reduce the probability of default.
- Lower EXT_SOURCE_2 values increase the probability of default.

This indicates a strong negative relationship between EXT_SOURCE_2 and loan default risk.

---

# Business Interpretation

Using SHAP, the bank can clearly explain why a customer's loan was approved or rejected.

For example:

Loan Approved because:

- Strong external credit score
- Stable employment profile
- Lower credit risk indicators

Loan Rejected because:

- Poor external credit score
- High loan amount
- Weak employment history

This improves transparency and customer confidence while helping the bank meet regulatory requirements.

---

# Benefits of SHAP

- Makes AI predictions explainable
- Improves model transparency
- Builds customer trust
- Supports regulatory compliance
- Identifies the most influential risk factors
- Explains individual customer predictions

---

# Conclusion

SHAP successfully transformed the XGBoost model from a black-box prediction system into an explainable AI solution.

The analysis confirmed that external credit score variables (EXT_SOURCE_3 and EXT_SOURCE_2) are the most influential factors affecting credit risk predictions. Loan amount, employment-related information, and customer profile also contributed to the model's decisions.

By integrating SHAP, the project not only predicts loan defaults accurately but also provides clear, interpretable explanations for every prediction, making the solution more reliable and suitable for real-world banking applications.

---


