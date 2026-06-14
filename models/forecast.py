# revenue forecast using Prophet

import pandas as pd
from prophet import Prophet


df = pd.read_excel("data/telco.xlsx", engine="openpyxl")
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
print(df.columns)
print(df.head())

df["date"] = pd.date_range(start="2022-01-01", periods=len(df))

revenue = df.groupby("date")["monthly_charges"].sum().reset_index()

revenue.columns = ["ds", "y"]

model = Prophet()
model.fit(revenue)

future = model.make_future_dataframe(periods=30)
forecast = model.predict(future)

model.plot(forecast)

#  What your current forecast is actually doing

# You built this pipeline:

# Excel dataset
#    ↓
# fake date column
#    ↓
# groupby(date) monthly_charges
#    ↓
# Prophet model
#    ↓
# 30-day revenue forecast
#  IMPORTANT (concept you must understand)

# Right now your forecast is:

# ❗ NOT real business time series

# Because:

# df["date"] = pd.date_range(...)

# 👉This is synthetic time

# So what you're really forecasting is:

# “If each row was a day, what is the trend of summed monthly charges?”

# Why this is still OK (for your project)

# For your portfolio:

# ✔ Good for demonstrating Prophet
# ✔ Good for showing forecasting pipeline
# ✔ Good for “analytics system demo”

# BUT in real companies you would use:

# invoice date
# billing cycle
# subscription start/end dates
# What you should do next (VERY IMPORTANT)

# Now your system has 3 working engines:

# 1. Churn prediction engine

# ✔ Logistic Regression
# ✔ XGBoost ready

# 2. Revenue risk engine

# ✔ churn probability × monthly revenue

# 3. Forecast engine

# ✔ Prophet revenue trend

# 🔥 NEXT STEP: CONNECT EVERYTHING (THIS IS THE REAL PROJECT)

# Right now everything is separate.

# We will now build:

# 👉 “Revenue Intelligence Table”

# One single dataset:

# customerid
# monthly_charges
# churn_probability
# expected_loss
# cltv
# risk_level
# forecasted_revenue_impact
# 🧠 WHY THIS STEP IS IMPORTANT

# This is what companies actually want:

# “Don’t just give me models — give me business decisions.”

# 🚀 WHAT I WILL HELP YOU BUILD NEXT

# If you say “connect everything”, I will help you build:

# 🔥 STEP 1 — Churn scoring table (XGBoost)
# 🔥 STEP 2 — Expected revenue loss per customer
# 🔥 STEP 3 — Cohort risk segmentation
# 🔥 STEP 4 — Forecast overlay (Prophet + churn impact)
# 🔥 STEP 5 — Final Streamlit dashboard
# 💡 FINAL RESULT (what your GitHub repo will look like)
# Revenue Intelligence System
# │
# ├── data_pipeline/
# ├── churn_model/
# ├── forecasting/
# ├── scoring_engine/
# ├── dashboard/
# └── README (very important)


