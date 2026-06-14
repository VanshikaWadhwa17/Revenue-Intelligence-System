import pandas as pd
from pandas.core.generic import T

df = pd.read_excel("data/telco.xlsx", engine="openpyxl")
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

MRR = df["monthly_charges"].sum()

ARPU = df["monthly_charges"].mean()

churn_rate = df["churn_value"].value_counts(normalize=True).get(1, 0)

LTV = ARPU * (1 / churn_rate)

print("MRR:", MRR)
#Total monthly revenue from all customers combined. This is the baseline revenue engine size
print("ARPU:", ARPU)
# Average customer pays ~$64.76/month. this tells us:
# pricing level, customer value tier
print("Churn Rate:", churn_rate)
# Typical benchmarks:

# SaaS healthy: 2%–8% monthly churn
# mid-stage: 8%–15%
# our dataset: 26% (high churn scenario)
# This is actually good for modeling because signal is strong
# but bad for real business stability
print("LTV:", LTV)
# Average customer lifetime revenue = $244

# Interpretation:

# ARPU ≈ 64.76
# LTV ≈ 244

# So:

# customers stay ~3–4 months on average

# This matches our churn rate (high churn → short lifetime)


# TILL NOW:
# 🏗 Revenue Engine
# MRR computed

# 👤 Customer Economics
# ARPU
# LTV

# ⚠️ Risk Layer
# churn rate

#  built a simplified version of: “Stripe / Intercom-style revenue analytics layer”
# Right now these metrics are:

# static
#  averaged
# not predictive