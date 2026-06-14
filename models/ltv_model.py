import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib

df = pd.read_excel("data/telco.xlsx", engine="openpyxl")
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

X = df[["monthly_charges", "tenure_months"]]
y = df["cltv"]

model = RandomForestRegressor()
model.fit(X, y)

joblib.dump(model, "models/ltv_model.pkl")

print("LTV model saved")