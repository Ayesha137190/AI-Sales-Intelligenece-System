import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "mysql+pymysql://root:root123@localhost:3306/sales_ai"
)

def inventory_optimization():

    df = pd.read_sql(
        "SELECT * FROM sales",
        engine
    )

    inventory = (
        df.groupby("product_name")
        .agg(
            avg_sales=("quantity","mean"),
            current_stock=("stock","mean")
        )
        .reset_index()
    )

    lead_time = 7

    inventory["reorder_point"] = (
        inventory["avg_sales"]
        * lead_time
    )

    inventory["safety_stock"] = (
        inventory["avg_sales"]
        * 2
    )

    inventory["recommended_order"] = (
        inventory["reorder_point"]
        + inventory["safety_stock"]
        - inventory["current_stock"]
    )

    inventory["recommended_order"] = (
        inventory["recommended_order"]
        .clip(lower=0)
    )

    return inventory