import streamlit as st
import pandas as pd

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(page_title="Revenue Intelligence Dashboard", layout="wide")

st.title("📊 Revenue Intelligence System Dashboard")

# -----------------------------
# LOAD DATA
# -----------------------------
@st.cache_data
def load_data():
    df = pd.read_excel("data/telco.xlsx", engine="openpyxl")

    # CLEAN COLUMN NAMES
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    return df

df = load_data()

# -----------------------------
# FIND CHURN COLUMN
# -----------------------------
possible_churn_cols = ["churn", "churn_label", "churn_value"]

churn_col = None
for col in possible_churn_cols:
    if col in df.columns:
        churn_col = col
        break

# -----------------------------
# FIX CHURN VALUES (IMPORTANT)
# -----------------------------
if churn_col:
    df[churn_col] = (
        df[churn_col]
        .astype(str)
        .str.lower()
        .map({"yes": 1, "no": 0})
    )

# -----------------------------
# SHOW RAW DATA
# -----------------------------
st.subheader("Dataset Preview")
st.write(df.head())

st.subheader("Dataset Columns")
st.write(list(df.columns))

# -----------------------------
# CHURN DISTRIBUTION CHART
# -----------------------------
st.subheader("Churn Distribution")

if churn_col is None:
    st.error("No churn column found in dataset.")
else:
    st.bar_chart(df[churn_col].value_counts())

# -----------------------------
# BASIC METRICS
# -----------------------------
st.subheader("Basic Metrics")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Customers", len(df))

with col2:
    if churn_col:
        churn_rate = df[churn_col].mean()
        st.metric("Churn Rate", f"{churn_rate:.2%}")
    else:
        st.metric("Churn Rate", "N/A")

with col3:
    st.metric("Total Features", len(df.columns))

# -----------------------------
# NUMERIC SUMMARY
# -----------------------------
st.subheader("Numeric Summary")
st.write(df.describe())