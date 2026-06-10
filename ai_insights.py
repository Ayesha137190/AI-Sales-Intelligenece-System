import pandas as pd

def get_insights(df):

    if df.empty:
        return "No data available."

    total_revenue = df["revenue"].sum()

    avg_sale = df["revenue"].mean()

    total_orders = len(df)

    region_sales = (
        df.groupby("region")["revenue"]
        .sum()
    )

    best_region = (
        region_sales.idxmax()
        if not region_sales.empty
        else "N/A"
    )

    worst_region = (
        region_sales.idxmin()
        if not region_sales.empty
        else "N/A"
    )

    category_sales = (
        df.groupby("category")["revenue"]
        .sum()
    )

    best_category = (
        category_sales.idxmax()
        if not category_sales.empty
        else "N/A"
    )

    return f"""
Total Revenue: ₹{total_revenue:,.0f}

Average Sale Value: ₹{avg_sale:,.0f}

Total Orders: {total_orders}

Best Region: {best_region}

Lowest Performing Region: {worst_region}

Best Category: {best_category}

Business Recommendations:

1. Increase marketing budget in the best-performing region.

2. Investigate reasons for low performance in the weakest region.

3. Maintain stock levels for top-selling categories.

4. Review anomaly reports weekly.

5. Compare forecasted revenue against actual revenue to improve planning.
"""