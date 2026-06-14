import pandas as pd
from sqlalchemy import create_engine


# -----------------------------
# DB CONNECTION
# -----------------------------
def get_engine():
    return create_engine(
        "postgresql://ds_user:password@localhost:5432/saas_db"
    )


# -----------------------------
# LOAD DATA
# -----------------------------
def load_churn_scores(engine):
    return pd.read_sql("SELECT * FROM churn_scores", engine)


# -----------------------------
# REVENUE AT RISK CALCULATION
# -----------------------------
def compute_revenue_at_risk(df):
    df["expected_loss"] = df["churn_probability"] * df["monthly_charges"]
    return df


# -----------------------------
# TOP RISK CUSTOMERS
# -----------------------------
def get_top_risky_customers(df, n=10):
    return df.sort_values("churn_probability", ascending=False).head(n)


# -----------------------------
# MAIN FUNCTION (THIS FIXES YOUR ERROR)
# -----------------------------
def get_revenue_risk_report():
    engine = get_engine()

    df = load_churn_scores(engine)
    df = compute_revenue_at_risk(df)

    return {
        "total_risk": df["expected_loss"].sum(),
        "top_customers": get_top_risky_customers(df),
        "full_data": df
    }