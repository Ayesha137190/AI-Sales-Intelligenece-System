import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "mysql+pymysql://root:root123@localhost:3306/sales_ai"
)

df = pd.read_csv(
    "data/sales.csv"
)

df.to_sql(
    "sales",
    engine,
    if_exists="append",
    index=False
)

print(
    "Data Inserted Successfully"
)