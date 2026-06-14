import pandas as pd

# -----------------------------
# LOAD + CLEAN
# -----------------------------
def load_clean_data(path="data/telco.xlsx"):
    df = pd.read_excel(path, engine="openpyxl")
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
    return df


# -----------------------------
# MRR
# -----------------------------
def calculate_mrr(df):
    return df["monthly_charges"].sum()


# -----------------------------
# ARPU
# -----------------------------
def calculate_arpu(df):
    return df["monthly_charges"].mean()


# -----------------------------
# CHURN RATE
# -----------------------------
def calculate_churn_rate(df):
    churn = df["churn_value"]
    return churn.value_counts(normalize=True).get(1, 0)


# -----------------------------
# SIMPLE LTV MODEL
# -----------------------------
def calculate_ltv(df):
    arpu = calculate_arpu(df)
    churn_rate = calculate_churn_rate(df)

    if churn_rate == 0:
        return 0

    return arpu * (1 / churn_rate)


# -----------------------------
# FULL SUMMARY (FOR DASHBOARD)
# -----------------------------
def get_finance_summary(df):
    return {
        "MRR": calculate_mrr(df),
        "ARPU": calculate_arpu(df),
        "Churn Rate": calculate_churn_rate(df),
        "LTV": calculate_ltv(df)
    }