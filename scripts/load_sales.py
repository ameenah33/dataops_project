import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("postgresql://amina:amina@localhost:5432/sales_db")

df = pd.read_csv("data/sales.csv")
df.to_sql("raw_sales", engine, if_exists="replace", index=False)

print("✅ sales.csv loaded into raw_sales")
