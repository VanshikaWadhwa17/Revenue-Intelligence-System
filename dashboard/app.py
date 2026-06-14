import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import pandas as pd
import joblib
from src.cohort_analysis import get_cohort_report
from src.forecast_engine import forecast_revenue
from src.scenario_simulator import simulate_revenue

from src.finance_metrics import get_finance_summary
from src.revenue_risk import get_revenue_risk_report
from src.health_score import compute_health_score, health_summary

st.set_page_config(page_title="Revenue Intelligence", layout="wide")

st.title("📊 Revenue Intelligence System")

# -----------------------------
# LOAD DATA
# -----------------------------
df = pd.read_excel("data/telco.xlsx")

# CLEAN
df.columns = df.columns.str.lower().str.strip().str.replace(" ", "_")

# Create churn flag (standardized once)
df["churn_flag"] = df["churn_label"].astype(str).str.lower().map({"yes": 1, "no": 0})

# -----------------------------
# FINANCE KPIs (ENGINE LAYER)
# -----------------------------
finance = get_finance_summary(df)

# -----------------------------
# EXECUTIVE KPIs
# -----------------------------
st.header("📈 Executive KPIs")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Customers", len(df))
col2.metric("MRR", f"${finance['MRR']:,.2f}")
col3.metric("ARPU", f"${finance['ARPU']:.2f}")
col4.metric("Churn Rate", f"{finance['Churn Rate']:.2%}")

# -----------------------------
# LTV METRIC
# -----------------------------
st.metric("Customer Lifetime Value (LTV)", f"${finance['LTV']:,.2f}")

# -----------------------------
# REVENUE AT RISK (ENGINE LAYER)
# -----------------------------
st.subheader("💰 Revenue at Risk (Model-Based)")

risk_report = get_revenue_risk_report()

st.metric(
    "Total Revenue at Risk",
    f"${risk_report['total_risk']:,.2f}"
)

st.dataframe(risk_report["top_customers"])

# -----------------------------
# CHURN RISK VIEW (EXPLORATION)
# -----------------------------
st.subheader("⚠️ High Risk Customers (Quick View)")

risk_customers = df[df["churn_flag"] == 1].sort_values("monthly_charges", ascending=False)
st.dataframe(risk_customers.head(10))

# -----------------------------
# EXPANSION MODEL
# -----------------------------
st.subheader("🚀 Expansion Opportunities")

model = joblib.load("models/expansion_model.pkl")

X = df[["monthly_charges", "tenure_months", "cltv"]]
df["expansion_score"] = model.predict_proba(X)[:, 1]

st.dataframe(
    df.sort_values("expansion_score", ascending=False).head(10)[
        ["customerid", "monthly_charges", "tenure_months", "cltv", "expansion_score"]
    ]
)
# -----------------------------
# COHORT ANALYSIS
# -----------------------------
st.subheader("📊 Cohort Analysis")

cohort_report = get_cohort_report(df)

col1, col2 = st.columns(2)

with col1:
    st.write("Churn by Cohort")
    st.bar_chart(cohort_report["churn"].set_index("tenure_group"))

with col2:
    st.write("Revenue by Cohort")
    st.bar_chart(cohort_report["revenue"].set_index("tenure_group"))
# -----------------------------
# FORECAST ENGINE
# -----------------------------
st.subheader("📈 Revenue Forecast (Next 6 Months)")

forecast_df = forecast_revenue(df)

st.line_chart(forecast_df.set_index("month"))
st.dataframe(forecast_df)

# -----------------------------
# SCENARIO SIMULATION
# -----------------------------
st.subheader("🎛️ Revenue Scenario Simulator")

col1, col2 = st.columns(2)

with col1:
    churn_delta = st.slider("Churn Change", -0.05, 0.10, 0.0, 0.01)

with col2:
    expansion_delta = st.slider("Expansion Change", -0.05, 0.10, 0.0, 0.01)

scenario_df = simulate_revenue(df, churn_delta, expansion_delta)

st.line_chart(scenario_df.set_index("month"))
st.dataframe(scenario_df)

# -----------------------------
# HEALTH SCORE
# -----------------------------
st.subheader("🧠 Unified Customer Health Score")

df = compute_health_score(df)

col1, col2, col3 = st.columns(3)

summary = health_summary(df)

col1.metric("Strong Customers", int(summary.get("Strong", 0)))
col2.metric("Healthy Customers", int(summary.get("Healthy", 0)))
col3.metric("At Risk Customers", int(summary.get("At Risk", 0)))

st.dataframe(
    df.sort_values("health_score", ascending=False)[
        ["customerid", "health_score", "health_segment",
         "monthly_charges", "tenure_months", "cltv"]
    ].head(20)
)
# -----------------------------
# INSIGHTS SECTION (VERY IMPORTANT FOR JD)
# -----------------------------
st.subheader("🧠 Business Insights")

st.write("""
- Customers with high monthly charges contribute most to revenue risk.
- Low tenure customers show higher churn probability.
- Expansion opportunities exist in mid-to-high CLTV segments.
- Revenue engine is driven by a small subset of high-value customers.
""")
