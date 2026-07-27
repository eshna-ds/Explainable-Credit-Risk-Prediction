import streamlit as st
import pandas as pd
import numpy as np
import joblib
import shap
import matplotlib.pyplot as plt

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Explainable Credit Risk Prediction",
    page_icon="🏦",
    layout="wide"
)

st.title("🏦 Explainable Credit Risk Prediction")

st.markdown(
"""
Predict whether a customer is likely to default on a loan.

This application uses an XGBoost model with Explainable AI (SHAP).
"""
)

# --------------------------------------------------
# LOAD MODEL
# --------------------------------------------------

@st.cache_resource
def load_model():
    model = joblib.load("models/xgboost.pkl")
    feature_columns = joblib.load("models/feature_columns.pkl")
    return model, feature_columns

model, feature_columns = load_model()

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

st.sidebar.header("Customer Details")

income = st.sidebar.number_input(
    "Annual Income",
    min_value=0.0,
    value=200000.0
)

credit = st.sidebar.number_input(
    "Credit Amount",
    min_value=0.0,
    value=300000.0
)

annuity = st.sidebar.number_input(
    "Annuity",
    min_value=0.0,
    value=25000.0
)

goods_price = st.sidebar.number_input(
    "Goods Price",
    min_value=0.0,
    value=300000.0
)

children = st.sidebar.number_input(
    "Number of Children",
    min_value=0,
    value=0
)

age = st.sidebar.number_input(
    "Age",
    min_value=18,
    max_value=100,
    value=30
)

employment = st.sidebar.number_input(
    "Employment Years",
    min_value=0,
    max_value=60,
    value=5
)

gender = st.sidebar.selectbox(
    "Gender",
    ["Male", "Female"]
)

car = st.sidebar.selectbox(
    "Own Car",
    ["Yes", "No"]
)

realty = st.sidebar.selectbox(
    "Own House",
    ["Yes", "No"]
)

education = st.sidebar.selectbox(
    "Education",
    [
        "Higher education",
        "Secondary / secondary special",
        "Incomplete higher",
        "Lower secondary",
        "Academic degree"
    ]
)

predict = st.sidebar.button("Predict")

# --------------------------------------------------
# CREATE FEATURE DATAFRAME
# --------------------------------------------------

input_df = pd.DataFrame(
    0,
    index=[0],
    columns=feature_columns
)

# --------------------------------------------------
# SAFE SET FUNCTION
# --------------------------------------------------

def set_feature(name, value):

    if name in input_df.columns:
        input_df.loc[0, name] = value

# --------------------------------------------------
# NUMERICAL FEATURES
# --------------------------------------------------

set_feature("CNT_CHILDREN", children)

set_feature("AMT_INCOME_TOTAL", income)

set_feature("AMT_CREDIT", credit)

set_feature("AMT_ANNUITY", annuity)

set_feature("AMT_GOODS_PRICE", goods_price)

set_feature("AGE_YEARS", age)

set_feature("EMPLOYMENT_YEARS", employment)

set_feature("CREDIT_INCOME_RATIO", credit / income if income != 0 else 0)

set_feature("ANNUITY_INCOME_RATIO", annuity / income if income != 0 else 0)

# --------------------------------------------------
# CATEGORICAL FEATURES
# --------------------------------------------------

set_feature("CODE_GENDER_M", 1 if gender == "Male" else 0)

set_feature("CODE_GENDER_F", 1 if gender == "Female" else 0)

set_feature("FLAG_OWN_CAR_Y", 1 if car == "Yes" else 0)

set_feature("FLAG_OWN_CAR_N", 1 if car == "No" else 0)

set_feature("FLAG_OWN_REALTY_Y", 1 if realty == "Yes" else 0)

set_feature("FLAG_OWN_REALTY_N", 1 if realty == "No" else 0)

education_column = f"NAME_EDUCATION_TYPE_{education}"

set_feature(education_column, 1)

# --------------------------------------------------
# DEBUG
# --------------------------------------------------

with st.expander("Debug"):

    st.write("Expected Features:", len(feature_columns))

    st.write("Input Shape:", input_df.shape)

    extra = list(set(input_df.columns) - set(feature_columns))

    missing = list(set(feature_columns) - set(input_df.columns))

    st.write("Extra Columns:", extra)

    st.write("Missing Columns:", missing)

# --------------------------------------------------
# PREDICTION
# --------------------------------------------------

if predict:

    prediction = model.predict(input_df)

    probability = model.predict_proba(input_df)

    st.header("Prediction")

    if prediction[0] == 1:

        st.error("⚠ High Risk Customer")

    else:

        st.success("✅ Low Risk Customer")

    st.subheader("Prediction Probability")

    st.write(
        f"Safe Customer : {probability[0][0]*100:.2f}%"
    )

    st.write(
        f"Default Risk : {probability[0][1]*100:.2f}%"
    )


    # --------------------------------------------------
    # SHAP EXPLAINABILITY
    # --------------------------------------------------

    st.header("Explainable AI (SHAP)")

    try:

        explainer = shap.TreeExplainer(model)

        # For newer SHAP versions
        try:
            shap_values = explainer(input_df)

            st.subheader("SHAP Waterfall Plot")

            plt.figure(figsize=(10,6))

            shap.plots.waterfall(
                shap_values[0],
                show=False
            )

            st.pyplot(plt.gcf())
            plt.clf()

            st.subheader("Top Feature Importance")

            plt.figure(figsize=(10,6))

            shap.plots.bar(
                shap_values[0],
                show=False
            )

            st.pyplot(plt.gcf())
            plt.clf()

        except:

            # Older SHAP versions

            shap_values = explainer.shap_values(input_df)

            explanation = shap.Explanation(
                values=shap_values[0],
                base_values=explainer.expected_value,
                data=input_df.iloc[0],
                feature_names=input_df.columns
            )

            st.subheader("SHAP Waterfall Plot")

            plt.figure(figsize=(10,6))

            shap.plots.waterfall(
                explanation,
                show=False
            )

            st.pyplot(plt.gcf())
            plt.clf()

    except Exception as e:

        st.warning("SHAP visualization could not be generated.")

        st.code(str(e))

    # --------------------------------------------------
    # XGBOOST FEATURE IMPORTANCE
    # --------------------------------------------------

    st.header("Model Feature Importance")

    try:

        importance = model.feature_importances_

        feature_importance = pd.DataFrame({

            "Feature": feature_columns,

            "Importance": importance

        })

        feature_importance = feature_importance.sort_values(

            by="Importance",

            ascending=False

        )

        st.dataframe(

            feature_importance.head(20),

            use_container_width=True

        )

        plt.figure(figsize=(10,6))

        plt.barh(

            feature_importance.head(10)["Feature"],

            feature_importance.head(10)["Importance"]

        )

        plt.xlabel("Importance")

        plt.ylabel("Feature")

        plt.title("Top 10 Important Features")

        plt.gca().invert_yaxis()

        st.pyplot(plt.gcf())

        plt.clf()

    except Exception as e:

        st.warning("Feature importance unavailable.")

        st.code(str(e))

    # --------------------------------------------------
    # DOWNLOAD REPORT
    # --------------------------------------------------

    report = pd.DataFrame({

        "Prediction":[

            "High Risk" if prediction[0] == 1 else "Low Risk"

        ],

        "Default Probability":[

            probability[0][1]

        ],

        "Safe Probability":[

            probability[0][0]

        ]

    })

    csv = report.to_csv(index=False).encode("utf-8")

    st.download_button(

        label="📥 Download Prediction Report",

        data=csv,

        file_name="prediction_report.csv",

        mime="text/csv"

    )

    # ======================================================
    # DASHBOARD SUMMARY
    # ======================================================
    
    st.markdown("---")
    st.header("📊 Prediction Dashboard")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(
            "Loan Status",
            "High Risk" if prediction[0] == 1 else "Low Risk"
        )
    
    with col2:
        st.metric(
            "Default Probability",
            f"{probability[0][1]*100:.2f}%"
        )
    
    with col3:
        st.metric(
            "Safe Probability",
            f"{probability[0][0]*100:.2f}%"
        )
    
    st.markdown("---")
    st.subheader("📈 Risk Meter")
    
    risk = probability[0][1]
    
    st.progress(float(risk))
    
    if risk < 0.30:
        st.success("🟢 Low Risk")
    
    elif risk < 0.70:
        st.warning("🟡 Medium Risk")
    
    else:
        st.error("🔴 High Risk")
    
    
    st.markdown("---")
    st.subheader("💡 Prediction Explanation")
    
    if prediction[0] == 1:
    
        st.error(
            """
    This customer has a HIGH probability of loan default.
    
    The bank should carefully review this application
    before approving the loan.
    """
        )
    
    else:
    
        st.success(
            """
    This customer has a LOW probability of loan default.
    
    The customer appears financially reliable
    based on the available information.
    """
        )
    
    
    st.markdown("---")
    st.subheader("👤 Customer Summary")
    
    summary = pd.DataFrame({
    
        "Feature":[
            "Annual Income",
            "Credit Amount",
            "Annuity",
            "Goods Price",
            "Age",
            "Employment Years",
            "Children",
            "Gender",
            "Own Car",
            "Own House",
            "Education"
        ],
    
        "Value":[
            income,
            credit,
            annuity,
            goods_price,
            age,
            employment,
            children,
            gender,
            car,
            realty,
            education
        ]
    
    })
    
    st.dataframe(summary, use_container_width=True)
    
    st.markdown("---")
    st.subheader("🤖 Model Information")
    
    model_info = pd.DataFrame({
    
        "Property":[
            "Algorithm",
            "Training Dataset",
            "Number of Features",
            "Explainability",
            "Framework"
        ],
    
        "Value":[
            "XGBoost",
            "Home Credit Default Risk",
            len(feature_columns),
            "SHAP",
            "Streamlit"
        ]
    
    })
    
    st.table(model_info)
    
    