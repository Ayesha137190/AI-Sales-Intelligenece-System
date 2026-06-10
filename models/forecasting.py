import pandas as pd
import numpy as np

from sqlalchemy import create_engine

from sklearn.model_selection import train_test_split

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

from xgboost import XGBRegressor

import joblib

# ----------------------------------
# MYSQL CONNECTION
# ----------------------------------

engine = create_engine(
    "mysql+pymysql://root:root123@localhost:3306/sales_ai"
)

# ----------------------------------
# LOAD DATA
# ----------------------------------

query = """
SELECT *
FROM sales
"""

df = pd.read_sql(
    query,
    engine
)

# ----------------------------------
# DATE FEATURES
# ----------------------------------

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
daily["week"] = daily["sale_date"].dt.isocalendar().week

# ----------------------------------
# LAG FEATURES
# ----------------------------------

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

# ----------------------------------
# FEATURES
# ----------------------------------

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

# ----------------------------------
# TRAIN TEST SPLIT
# ----------------------------------

split_index = int(len(X) * 0.8)

X_train = X[:split_index]

X_test = X[split_index:]

y_train = y[:split_index]

y_test = y[split_index:]

# ----------------------------------
# MODEL
# ----------------------------------

model = XGBRegressor(
    n_estimators=500,
    learning_rate=0.05,
    max_depth=8,
    subsample=0.8,
    colsample_bytree=0.8,
    random_state=42
)

model.fit(
    X_train,
    y_train
)

# ----------------------------------
# PREDICTIONS
# ----------------------------------

predictions = model.predict(
    X_test
)

# ----------------------------------
# METRICS
# ----------------------------------

mae = mean_absolute_error(
    y_test,
    predictions
)

rmse = np.sqrt(
    mean_squared_error(
        y_test,
        predictions
    )
)

r2 = r2_score(
    y_test,
    predictions
)

print("\nModel Results\n")

print("MAE :", round(mae,2))

print("RMSE :", round(rmse,2))

print("R2 :", round(r2,4))

# ----------------------------------
# SAVE MODEL
# ----------------------------------

joblib.dump(
    model,
    "saved_models/xgb_sales_model.pkl"
)

print("\nModel Saved Successfully")