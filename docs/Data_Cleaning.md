# Data Cleaning

## Dataset

Home Credit Default Risk

## Dataset Size

Rows: 307,511

Columns: 122

## Data Types

Float Columns: 65

Integer Columns: 41

Categorical Columns: 16

## Missing Values

Several columns contain a high percentage of missing values.

For example:

COMMONAREA_AVG – 69.87%

COMMONAREA_MODE – 69.87%

COMMONAREA_MEDI – 69.87%

NONLIVINGAPARTMENTS_MEDI – 69.43%

NONLIVINGAPARTMENTS_MODE – 69.43%

These columns will be evaluated during preprocessing to decide whether they should be removed or imputed.

## Duplicate Rows

No duplicate rows were found.

Duplicate Count = 0

## Conclusion

The dataset is clean in terms of duplicate records. However, several features contain a large number of missing values and will require preprocessing before training the machine learning model.

