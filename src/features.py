import os

print("=" * 50)
print("RUNNING FILE:", __file__)
print("WORKING DIRECTORY:", os.getcwd())
print("=" * 50)

import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("postgresql://ds_user:password@localhost:5432/saas_db")

# ----------------------------
# ALWAYS READ FULL RAW DATA
# ----------------------------
df = pd.read_sql("SELECT * FROM customers_raw", engine)
print("RAW DATA SHAPE:", df.shape)

print("ROWS READ:", len(df))

print(
    pd.read_sql(
        """
        SELECT churn_label, COUNT(*) cnt
        FROM customers_raw
        GROUP BY churn_label
        """,
        engine,
    )
)

# ----------------------------
# CLEAN
# ----------------------------
df["total_charges"] = pd.to_numeric(df["total_charges"], errors="coerce")
df = df.dropna()

# ----------------------------
# DEBUG: CHECK RAW DISTRIBUTION
# ----------------------------
print("RAW CHURN DISTRIBUTION:")
print(df["churn_label"].value_counts())

# ----------------------------
# FIX TARGET (CRITICAL)
# ----------------------------
df["churn_label"] = df["churn_label"].astype(str).str.strip()

df["churn_value"] = df["churn_label"].apply(
    lambda x: 1 if x.lower() == "yes" else 0
)

print("MAPPED CHURN DISTRIBUTION:")
print(df["churn_value"].value_counts())

# ----------------------------
# FEATURES
# ----------------------------
df["avg_revenue_per_month"] = df["total_charges"] / (df["tenure_months"] + 1)
df["is_long_term"] = (df["tenure_months"] > 12).astype(int)
df["is_high_value"] = (df["monthly_charges"] > df["monthly_charges"].median()).astype(int)

# ----------------------------
# SAVE FULL DATASET (NO FILTERING)
# ----------------------------
df.to_sql("customer_features", engine, if_exists="replace", index=False)

print("FEATURE TABLE REBUILT CORRECTLY")