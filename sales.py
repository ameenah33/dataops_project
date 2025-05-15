import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv("sales.csv")

# Adapter l'URL de connexion
engine = create_engine("postgresql://amina:amina@localhost:5432/sales_db")

# Charger dans une table raw_sales
df.to_sql("raw_sales", engine, if_exists="replace", index=False)
