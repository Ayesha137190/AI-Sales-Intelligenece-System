import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "mysql+pymysql://root:root123@localhost:3306/sales_ai"
)

def low_stock_products():

    df = pd.read_sql(
        "SELECT * FROM sales",
        engine
    )

    avg_daily_sales = df["quantity"].mean()

    lead_time = 7

    reorder_point = avg_daily_sales * lead_time

    low_stock = df[
        df["stock"] < reorder_point
    ]

    return low_stock