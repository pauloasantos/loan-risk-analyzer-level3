import streamlit as st
import pandas as pd
from portfolio_analyzer import PortfolioAnalyzer

sample_data = [
    {"id": "A001", "income": 50000, "loan_amount": 20000, "credit_score": 650, "age": 40},
    {"id": "A002", "income": 30000, "loan_amount": 18000, "credit_score": 590, "age": 22},
    {"id": "B001", "income": 80000, "loan_amount": 50000, "credit_score": 700, "age": 45, "revenue": 120000},
    {"id": "B002", "income": 60000, "loan_amount": 40000, "credit_score": 610, "age": 38, "revenue": 90000}
]

st.set_page_config(layout="wide", page_title="Loan Portfolio Risk Analyzer", initial_sidebar_state="expanded")
# Initialize session state for applicant rows
if "rows" not in st.session_state:
    st.session_state.rows = sample_data.copy()
    

st.sidebar.header("Data Source")

# Data Upload
uploaded_file = st.sidebar.file_uploader("Upload CSV, (columns: id, income, loan_amount, credit_score, age, revenue)", type=["csv"])

if uploaded_file:
    df_uploaded = pd.read_csv(uploaded_file)
    st.session_state.rows = df_uploaded.to_dict(orient="records")
    st.sidebar.success("Data uploaded successfully!")
else:
    st.sidebar.info("Using default sample data")

with st.sidebar.form("add_applicant_form"):
    st.write("Add New Applicant")
    applicant_type = st.selectbox("Applicant Type", ["individual", "business"], key="applicant_type_form")
    id_val = st.text_input("ID")
    income_val = st.number_input("Income", min_value=0.0, step=1000.0)
    loan_val = st.number_input("Loan Amount", min_value=0.0, step=1000.0)
    credit_val = st.number_input("Credit Score", min_value=0, max_value=850, step=1)
    age_val = st.number_input("Age", min_value=0, max_value=120, step=1)
    revenue_val = None
    if applicant_type == "business":
        revenue_val = st.number_input("Revenue", min_value=0.0, step=1000.0)
    submitted = st.form_submit_button("Add Applicant")
    if submitted:
        new_applicant = {
            "id": id_val,
            "income": income_val,
            "loan_amount": loan_val,
            "credit_score": credit_val,
            "age": age_val
        }
        if applicant_type == "business":
            new_applicant["revenue"] = revenue_val
        st.session_state.rows.append(new_applicant)
        st.sidebar.success(f"Applicant {id_val} added!")



st.header("Loan Portfolio Risk Analyzer - Level 3")
tab1, tab2, tab3 = st.tabs(["Data Overview", "Risk Analysis", "Summary"])
portfolio = PortfolioAnalyzer.from_dicts(st.session_state.rows)

with tab1:
    st.subheader("Applicant Data")
    st.dataframe(pd.DataFrame(st.session_state.rows))

with tab2:
    st.subheader("Risk Analysis")
    category = st.selectbox("Filter by Risk Category", ["All", "Low", "Medium", "High"])
    filtered_df = portfolio.filter_by_category(category)
    st.dataframe(filtered_df)
    st.bar_chart(filtered_df["risk_category"].value_counts())

with tab3:
    st.subheader("Portfolio Summary")
    summary = portfolio.summarize()
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Applicants", summary["total"])
    col2.metric("High-Risk Applicants", summary["high_risk"])
    col3.metric("Average Risk Score", summary["average_score"])
    if summary["highest_risk"]:
        hr = summary["highest_risk"]
        col4.metric("Highest Risk", f'{hr["id"]} ({hr["score"]}, {hr["category"]})')
    else:
        col4.metric("Highest Risk", "—")
    st.bar_chart(pd.Series(summary["distribution"]))