import pandas as pd
import shap
import joblib

def shap_importance():

    model = joblib.load(
        "saved_models/xgb_sales_model.pkl"
    )

    df = pd.read_csv(
        "data/sales.csv"
    )

    X = df[
        [
            "quantity",
            "price",
            "stock"
        ]
    ]

    explainer = shap.TreeExplainer(
        model
    )

    shap_values = explainer.shap_values(
        X
    )

    return shap_values, X