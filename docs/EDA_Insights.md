# Target Variable Analysis

The dataset contains 307,511 loan applications.

- Customers who repaid the loan (TARGET = 0): 282,686
- Customers who defaulted (TARGET = 1): 24,825

This shows that the dataset is highly imbalanced, with approximately 91.9% non-default cases and 8.1% default cases.

Because of this imbalance, accuracy alone is not an appropriate evaluation metric. Precision, Recall, F1-score, and ROC-AUC will also be used during model evaluation.

---

# Correlation Analysis

The strongest negatively correlated features with the target are:

- EXT_SOURCE_3
- EXT_SOURCE_2
- EXT_SOURCE_1

These features indicate that customers with higher external credit scores have a lower probability of defaulting.

Features such as DAYS_BIRTH and REGION_RATING_CLIENT show only weak positive correlations with the target.

The correlation analysis suggests that external credit-related features are likely to be the most informative predictors for the machine learning model.
