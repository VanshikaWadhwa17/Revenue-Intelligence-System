import pandas as pd


# -----------------------------
# COHORT CREATION
# -----------------------------
def create_cohort(df):
    df = df.copy()

    # Ensure clean column
    df["tenure_group"] = pd.cut(
        df["tenure_months"],
        bins=[0, 3, 6, 12, 24, 100],
        labels=["0-3", "3-6", "6-12", "12-24", "24+"]
    )

    return df


# -----------------------------
# CHURN BY COHORT
# -----------------------------
def cohort_churn(df):
    cohort = df.groupby("tenure_group")["churn_flag"].mean().reset_index()
    cohort.columns = ["tenure_group", "churn_rate"]
    return cohort


# -----------------------------
# REVENUE BY COHORT
# -----------------------------
def cohort_revenue(df):
    cohort = df.groupby("tenure_group")["monthly_charges"].mean().reset_index()
    cohort.columns = ["tenure_group", "avg_revenue"]
    return cohort


# -----------------------------
# MAIN FUNCTION
# -----------------------------
def get_cohort_report(df):
    df = create_cohort(df)

    return {
        "df": df,
        "churn": cohort_churn(df),
        "revenue": cohort_revenue(df)
    }