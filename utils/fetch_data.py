import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "mysql+pymysql://root:root123@localhost:3306/sales_ai"
)

query = """
SELECT *
FROM sales
"""

df = pd.read_sql(
    query,
    engine
)

print(df.head())