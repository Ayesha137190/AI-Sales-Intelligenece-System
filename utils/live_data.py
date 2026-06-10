import pandas as pd
from database.db import engine

def get_live_sales():

    query = """
    SELECT *
    FROM sales
    ORDER BY sale_date DESC
    """

    return pd.read_sql(query, engine)