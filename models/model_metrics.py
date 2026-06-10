import numpy as np
import pandas as pd
import joblib

from sqlalchemy import create_engine

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

engine = create_engine(
    "mysql+pymysql://root:root123@localhost:3306/sales_ai"
)

def get_model_metrics():

    model = joblib.load(
        "saved_models/xgb_sales_model.pkl"
    )

    df = pd.read_sql(
        "SELECT * FROM sales",
        engine
    )

    df["sale_date"] = pd.to_datetime(
        df["sale_date"]
    )

    daily = (
        df.groupby("sale_date")["revenue"]
        .sum()
        .reset_index()
    )

    daily["day"] = daily["sale_date"].dt.day
    daily["month"] = daily["sale_date"].dt.month
    daily["year"] = daily["sale_date"].dt.year
    daily["week"] = daily["sale_date"].dt.isocalendar().week.astype(int)

    daily["lag7"] = daily["revenue"].shift(7)
    daily["lag14"] = daily["revenue"].shift(14)
    daily["lag30"] = daily["revenue"].shift(30)

    daily["rolling7"] = daily["revenue"].rolling(7).mean()
    daily["rolling30"] = daily["revenue"].rolling(30).mean()

    daily = daily.dropna()

    X = daily[
        [
            "day",
            "month",
            "year",
            "week",
            "lag7",
            "lag14",
            "lag30",
            "rolling7",
            "rolling30"
        ]
    ]

    y = daily["revenue"]

    predictions = model.predict(X)

    mae = mean_absolute_error(
        y,
        predictions
    )

    rmse = np.sqrt(
        mean_squared_error(
            y,
            predictions
        )
    )

    r2 = r2_score(
        y,
        predictions
    )

    return mae, rmse, r2