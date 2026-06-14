import pandas as pd


# -----------------------------
# NORMALIZE FUNCTION
# -----------------------------
def normalize(series):
    return (series - series.min()) / (series.max() - series.min() + 1e-9)


# -----------------------------
# HEALTH SCORE ENGINE
# -----------------------------
def compute_health_score(df):

    df = df.copy()

    # Ensure required columns exist
    df["churn_flag"] = df["churn_flag"].fillna(0)

    # Normalize inputs
    churn_risk = df["churn_flag"]  # already 0/1
    expansion_score = normalize(df["cltv"])
    revenue_score = normalize(df["monthly_charges"])
    tenure_score = normalize(df["tenure_months"])

    # Weighted health score
    df["health_score"] = (
        (1 - churn_risk) * 0.4 +
        expansion_score * 0.3 +
        revenue_score * 0.2 +
        tenure_score * 0.1
    ) * 100

    # Segment customers
    df["health_segment"] = pd.cut(
        df["health_score"],
        bins=[0, 40, 70, 100],
        labels=["At Risk", "Healthy", "Strong"]
    )

    return df


# -----------------------------
# SUMMARY
# -----------------------------
def health_summary(df):
    return df["health_segment"].value_counts()