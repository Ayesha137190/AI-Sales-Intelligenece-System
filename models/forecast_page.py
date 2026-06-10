import os
import pandas as pd
import plotly.graph_objects as go
import joblib
from sqlalchemy import create_engine

engine = create_engine(
    "mysql+pymysql://root:root123@localhost:3306/sales_ai"
)

def forecast_chart():

    base_dir = os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )

    model_path = os.path.join(
        base_dir,
        "saved_models",
        "xgb_sales_model.pkl"
    )

    if not os.path.exists(model_path):
        raise FileNotFoundError(
            f"Model not found: {model_path}"
        )

    model = joblib.load(model_path)

    df = pd.read_sql(
        "SELECT * FROM sales",
        engine
    )

    if df.empty:
        raise ValueError(
            "No data found in sales table."
        )

    df["sale_date"] = pd.to_datetime(
        df["sale_date"]
    )

    daily = (
        df.groupby("sale_date")["revenue"]
        .sum()
        .reset_index()
        .sort_values("sale_date")
    )

    daily["day"] = daily["sale_date"].dt.day
    daily["month"] = daily["sale_date"].dt.month
    daily["year"] = daily["sale_date"].dt.year
    daily["week"] = (
        daily["sale_date"]
        .dt.isocalendar()
        .week
        .astype(int)
    )

    daily["lag7"] = daily["revenue"].shift(7)
    daily["lag14"] = daily["revenue"].shift(14)
    daily["lag30"] = daily["revenue"].shift(30)

    daily["rolling7"] = (
        daily["revenue"]
        .rolling(7)
        .mean()
    )

    daily["rolling30"] = (
        daily["revenue"]
        .rolling(30)
        .mean()
    )

    daily = daily.dropna()

    if daily.empty:
        raise ValueError(
            "Not enough data to create forecast features."
        )

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

    daily["prediction"] = model.predict(X)

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=daily["sale_date"],
            y=daily["revenue"],
            mode="lines",
            name="Actual Revenue"
        )
    )

    fig.add_trace(
        go.Scatter(
            x=daily["sale_date"],
            y=daily["prediction"],
            mode="lines",
            name="Predicted Revenue"
        )
    )

    fig.update_layout(
        title="Actual vs Predicted Revenue",
        xaxis_title="Date",
        yaxis_title="Revenue",
        height=600
    )

    return fig