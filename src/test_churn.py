from sqlalchemy import create_engine
import pandas as pd

engine = create_engine("postgresql://ds_user:password@localhost:5432/saas_db")

df = pd.read_sql("SELECT churn_label, churn_value FROM customer_features", engine)

print(df["churn_label"].value_counts())
print(df["churn_value"].value_counts())