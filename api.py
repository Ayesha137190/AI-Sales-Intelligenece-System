from fastapi import FastAPI
from sqlalchemy import create_engine
import pandas as pd

app = FastAPI()

engine = create_engine(
    "mysql+pymysql://root:root123@localhost:3306/sales_ai"
)

@app.get("/sales")
def get_sales():

    df = pd.read_sql(
        "SELECT * FROM sales",
        engine
    )

    return df.to_dict(
        orient="records"
    )