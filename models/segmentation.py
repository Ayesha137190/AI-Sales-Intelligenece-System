import pandas as pd
from sqlalchemy import create_engine
from sklearn.cluster import KMeans

engine = create_engine(
    "mysql+pymysql://root:root123@localhost:3306/sales_ai"
)

def get_segments():

    df = pd.read_sql(
        "SELECT * FROM sales",
        engine
    )

    product_data = (
        df.groupby("product_name")
        .agg(
            revenue=("revenue","sum"),
            quantity=("quantity","sum"),
            stock=("stock","mean")
        )
        .reset_index()
    )

    X = product_data[
        [
            "revenue",
            "quantity",
            "stock"
        ]
    ]

    model = KMeans(
        n_clusters=4,
        random_state=42,
        n_init=10
    )

    product_data["segment"] = model.fit_predict(X)

    return product_data