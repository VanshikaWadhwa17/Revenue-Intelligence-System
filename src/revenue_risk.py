import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("postgresql://ds_user:password@localhost:5432/saas_db")

df = pd.read_sql("SELECT * FROM churn_scores", engine)

# expected monthly loss
df["expected_loss"] = df["churn_probability"] * df["monthly_charges"]

print("TOTAL REVENUE AT RISK:", df["expected_loss"].sum())

print("\nTop 10 risky customers:")
print(df.sort_values("churn_probability", ascending=False).head(10))