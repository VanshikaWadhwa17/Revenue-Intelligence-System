import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

df = pd.read_excel("data/telco.xlsx", engine="openpyxl")
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# simple feature engineering
df["high_value"] = df["monthly_charges"] > df["monthly_charges"].median()

X = df[["monthly_charges", "tenure_months", "cltv"]]
y = df["high_value"].astype(int)

model = RandomForestClassifier()
model.fit(X, y)

joblib.dump(model, "models/expansion_model.pkl")

print("Expansion model saved")