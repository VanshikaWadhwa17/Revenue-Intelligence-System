import pandas as pd


# -----------------------------
# BASE MRR
# -----------------------------
def calculate_mrr(df):
    return df["monthly_charges"].sum()


# -----------------------------
# SIMPLE FORECAST MODEL
# -----------------------------
def forecast_revenue(df, months=6):

    mrr = calculate_mrr(df)

    churn_rate = df["churn_flag"].mean()
    expansion_rate = 0.05  # assumption (you can later model this)

    forecasts = []

    current_mrr = mrr

    for month in range(1, months + 1):

        churn_loss = current_mrr * churn_rate
        expansion_gain = current_mrr * expansion_rate

        current_mrr = current_mrr - churn_loss + expansion_gain

        forecasts.append({
            "month": month,
            "forecast_mrr": current_mrr
        })

    return pd.DataFrame(forecasts)