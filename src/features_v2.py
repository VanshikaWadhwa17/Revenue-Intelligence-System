import pandas as pd
from sqlalchemy import create_engine

# Connect to PostgreSQL
engine = create_engine(
    "postgresql://ds_user:password@localhost:5432/saas_db"
)

# -------------------------
# Load raw data
# -------------------------
df = pd.read_sql(
    "SELECT * FROM customers_raw",
    engine
)

print("RAW SHAPE:", df.shape)

print("\nRAW CHURN DISTRIBUTION:")
print(df["churn_label"].value_counts(dropna=False))

# -------------------------
# Clean data
# -------------------------

# Convert Total Charges to numeric
df["total_charges"] = pd.to_numeric(
    df["total_charges"],
    errors="coerce"
)

# Remove rows where total_charges is missing
df = df.dropna(subset=["total_charges"])

print("\nAFTER CLEANING:")
print(df.shape)

# -------------------------
# Create target variable
# -------------------------

df["churn_label"] = (
    df["churn_label"]
    .astype(str)
    .str.strip()
)

df["churn_value"] = (
    df["churn_label"]
    .map({
        "No": 0,
        "Yes": 1
    })
)

print("\nMAPPED CHURN DISTRIBUTION:")
print(df["churn_value"].value_counts(dropna=False))

# -------------------------
# Feature Engineering
# -------------------------

df["avg_revenue_per_month"] = (
    df["total_charges"] /
    (df["tenure_months"] + 1)
)

df["is_long_term"] = (
    df["tenure_months"] > 12
).astype(int)

df["is_high_value"] = (
    df["monthly_charges"] >
    df["monthly_charges"].median()
).astype(int)

# -------------------------
# Save NEW table
# -------------------------

df.to_sql(
    "customer_features_v2",
    engine,
    if_exists="replace",
    index=False
)

print("\ncustomer_features_v2 created successfully")
print("FINAL SHAPE:", df.shape)