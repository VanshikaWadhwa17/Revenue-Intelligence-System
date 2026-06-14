import pandas as pd


# -----------------------------
# SCENARIO SIMULATION ENGINE
# -----------------------------
def simulate_revenue(df, churn_delta=0.0, expansion_delta=0.0):

    base_mrr = df["monthly_charges"].sum()

    base_churn = df["churn_flag"].mean()

    # apply scenario adjustments
    adjusted_churn = max(base_churn + churn_delta, 0)
    expansion_rate = max(0.05 + expansion_delta, 0)

    results = []

    current_mrr = base_mrr

    for month in range(1, 7):

        churn_loss = current_mrr * adjusted_churn
        expansion_gain = current_mrr * expansion_rate

        current_mrr = current_mrr - churn_loss + expansion_gain

        results.append({
            "month": month,
            "scenario_mrr": current_mrr
        })

    return pd.DataFrame(results)