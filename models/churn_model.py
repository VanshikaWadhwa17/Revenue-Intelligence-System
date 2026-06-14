# Churn model: Will the customer leave(churn) or stay(not churn)?
# (Logistic Regression baseline)

import pandas as pd
from sqlalchemy import create_engine

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, roc_auc_score

# -----------------------
# CONNECT TO POSTGRES
# -----------------------
engine = create_engine("postgresql://ds_user:password@localhost:5432/saas_db")

df = pd.read_sql("SELECT * FROM customer_features_v2", engine)

print("Shape:", df.shape)

print("\nChurn value distribution:")
print(df["churn_value"].value_counts(dropna=False))

print("\nUnique churn values:")
print(df["churn_value"].unique())

print("\nFirst 5 rows:")
print(df[["churn_label", "churn_value"]].head())

# -----------------------
# CLEAN TARGET
# -----------------------
df["churn_value"] = df["churn_value"].astype(int)

# -----------------------
# SELECT FEATURES
# -----------------------
features = [
    "tenure_months",
    "monthly_charges",
    "total_charges",
    "is_long_term",
    "is_high_value"
]

X = df[features]
y = df["churn_value"]

# -----------------------
# TRAIN / TEST SPLIT
# -----------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -----------------------
# MODEL
# -----------------------
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# -----------------------
# PREDICTIONS
# -----------------------
y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:, 1]

# -----------------------
# EVALUATION
# -----------------------
print("CLASSIFICATION REPORT:")
print(classification_report(y_test, y_pred))

print("\nROC AUC SCORE:")
print(roc_auc_score(y_test, y_prob))