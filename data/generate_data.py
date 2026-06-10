from faker import Faker
import random
import pandas as pd

fake = Faker()

sales = []

for i in range(100000):

    qty = random.randint(1, 20)

    price = random.randint(500, 5000)

    revenue = qty * price

    sales.append([
        fake.date_between("-2y", "today"),
        fake.word(),
        random.choice(
            [
                "Electronics",
                "Clothing",
                "Furniture",
                "Sports"
            ]
        ),
        random.choice(
            [
                "North",
                "South",
                "East",
                "West"
            ]
        ),
        qty,
        price,
        revenue,
        random.randint(20, 500)
    ])

df = pd.DataFrame(
    sales,
    columns=[
        "sale_date",
        "product_name",
        "category",
        "region",
        "quantity",
        "price",
        "revenue",
        "stock"
    ]
)

print(df.head())

df.to_csv(
    "data/sales.csv",
    index=False
)

print("100000 Records Created")