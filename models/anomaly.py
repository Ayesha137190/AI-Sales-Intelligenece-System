import pandas as pd
from sqlalchemy import create_engine
from sklearn.ensemble import IsolationForest

engine = create_engine(
    "mysql+pymysql://root:root123@localhost:3306/sales_ai"
)

def get_anomalies():

    df = pd.read_sql(
        "SELECT * FROM sales",
        engine
    )

    model = IsolationForest(
        contamination=0.02,
        random_state=42
    )

    df["anomaly"] = model.fit_predict(
        df[["revenue"]]
    )

    anomalies = df[
        df["anomaly"] == -1
    ]

    return anomalies