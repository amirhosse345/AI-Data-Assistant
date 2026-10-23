import pandas as pd

df = pd.read_csv("data/sales.csv")


def calculate_total_sales():
    total = df["Sales"].sum()
    return total


def get_best_selling_product():
    max_sales = df["Sales"].max()
    product = df.loc[df["Sales"] == max_sales, "Product"]
    return product.iloc[0]


def get_sales_by_category(category):
    filtered = df.loc[df["Category"] == category, "Sales"]
    total = filtered.sum()
    return total