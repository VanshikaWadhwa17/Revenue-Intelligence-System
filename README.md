# 📊 Revenue Intelligence System (SaaS Analytics Platform)

A production-style **Revenue Intelligence and Forecasting system** that simulates how modern SaaS companies (like Stripe, Intercom, and HubSpot) analyze customer behavior, predict churn, forecast revenue, and optimize expansion strategy.

Built using **Python, PostgreSQL, Machine Learning, and Streamlit**, this project transforms raw customer data into **actionable financial intelligence**.

---

#  Key Features

##  Revenue Engine

* Monthly Recurring Revenue (MRR)
* Average Revenue Per User (ARPU)
* Customer Lifetime Value (LTV)
* Churn Rate analysis

---

##  Revenue Risk Engine

* Churn probability-based revenue loss estimation
* Expected monthly revenue at risk
* Top high-risk customers identification
* PostgreSQL-backed scoring pipeline

---

##  Cohort Analytics

* Customer segmentation by tenure
* Cohort-based churn analysis
* Revenue behavior across lifecycle stages

---

##  Revenue Forecasting Engine

* 6-month forward revenue projection
* Churn + expansion-based simulation model
* Dynamic MRR evolution tracking

---

##  Scenario Simulator

* What-if analysis for business planning:

  * Churn increase/decrease
  * Expansion changes
* Real-time revenue impact simulation

---

##  Customer Health Scoring System

Unified scoring model combining:

* Churn risk
* Customer value (CLTV)
* Revenue contribution
* Tenure behavior

Outputs:

* 🔴 At Risk Customers
* 🟡 Healthy Customers
* 🟢 High-Value Customers

---

##  Interactive Dashboard (Streamlit)

* Executive KPI overview
* Risk segmentation
* Forecast visualization
* Expansion opportunity ranking
* Cohort + scenario analysis

---

#  System Architecture

```
Excel Dataset (Telco Customer Data)
        ↓
PostgreSQL Database (Customer Warehouse)
        ↓
Python Data Engineering Layer (Pandas)
        ↓
Machine Learning Models (Churn + Expansion)
        ↓
Revenue Intelligence Engine
        ↓
Streamlit Dashboard (Executive Layer)
```

---

#  Tech Stack

### Core

* Python 3.10+
* Pandas
* NumPy

### Database

* PostgreSQL
* SQLAlchemy

### Machine Learning

* XGBoost
* Scikit-learn
* Joblib

### Forecasting

* Custom probabilistic revenue model

### Visualization

* Streamlit

---


# ⚙️ Setup Instructions

## 1. Clone Repository

```bash
git clone https://github.com/VanshikaWadhwa17/Revenue-Intelligence-System
cd revenue-intelligence-system
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Setup PostgreSQL

Create database:

```sql
CREATE DATABASE saas_db;
```

Create user:

```sql
CREATE USER ds_user WITH PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE saas_db TO ds_user;
```

---

## 5. Load Data into Database

```bash
python src/load_data.py
```

---

## 6. Run Dashboard

```bash
streamlit run dashboard/app.py
```

---

# 📊 Business Impact

This system simulates a real-world **Revenue Operations Intelligence Platform** used for:

* Predicting churn before it happens
* Estimating revenue at risk
* Forecasting ARR growth
* Identifying expansion opportunities
* Supporting CFO-level decision making

---

# 🎯 Key Insights Generated

* High churn customers contribute disproportionately to revenue risk
* Early-tenure customers show significantly higher churn probability
* Expansion opportunities exist in mid-to-high CLTV segments
* Revenue forecasting shows compounding effect of churn vs expansion

---

# 💡 What Makes This Project Special

Unlike typical ML projects, this system:

✔ Combines finance + ML + product analytics
✔ Simulates real SaaS revenue behavior
✔ Includes forecasting + scenario simulation
✔ Uses production-style modular architecture
✔ Produces executive-ready insights

---

# 📌 Future Improvements

* Real-time streaming data pipeline (Kafka)
* Snowflake / BigQuery integration
* Advanced probabilistic forecasting (Prophet / Nixtla)
* LLM-based executive insight generator
* Automated anomaly detection for revenue drops

---

# 👨‍💻 Author

Built by **Vanshika Wadhwa**
Data Science | Revenue Analytics | Machine Learning

---

# 🧠 Final Note

This project demonstrates a full **end-to-end Revenue Intelligence System**, moving from raw data → predictive models → financial forecasting → executive decision-making tools.


