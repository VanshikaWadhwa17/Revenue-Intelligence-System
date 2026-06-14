from sqlalchemy import create_engine, text

engine = create_engine("postgresql://ds_user:password@localhost:5432/saas_db")

with engine.connect() as conn:
    result = conn.execute(text("SELECT 1"))
    print(result.fetchone())