# churn probability table:

import pandas as pd
from sqlalchemy import create_engine
from xgboost import XGBClassifier

engine = create_engine("postgresql://ds_user:password@localhost:5432/saas_db")

df = pd.read_sql("SELECT * FROM customer_features_v2", engine)

features = [
    "tenure_months",
    "monthly_charges",
    "total_charges",
    "is_long_term",
    "is_high_value"
]

X = df[features]
y = df["churn_value"]

model = XGBClassifier(n_estimators=200, max_depth=4)
model.fit(X, y)

df["churn_probability"] = model.predict_proba(X)[:, 1]

output = df[[
    "customerid",
    "churn_probability",
    "monthly_charges",
    "tenure_months"
]]

output.to_sql("churn_scores", engine, if_exists="replace", index=False)

print("Scoring table created")