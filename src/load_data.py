import pandas as pd
from sqlalchemy import create_engine

# 1. Read Excel file
df = pd.read_excel("data/telco.xlsx", engine="openpyxl")

# 2. Clean column names (important!)
df.columns = df.columns.str.lower().str.replace(" ", "_")

# 3. Connect to PostgreSQL
engine = create_engine("postgresql://ds_user:password@localhost:5432/saas_db")

# 4. Load into SQL
df.to_sql("customers_raw", engine, if_exists="replace", index=False)

print("Excel data loaded into PostgreSQL successfully")



# After this script completed without errors
# df.to_sql() worked
# Table was created in PostgreSQL
# Data was inserted successfully