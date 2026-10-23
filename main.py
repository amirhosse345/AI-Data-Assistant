import os
import pandas as pd
from dotenv import load_dotenv

load_dotenv(".env", override=True)

api_key = os.getenv("OPENAI_API_KEY")

print("Key found:", api_key is not None)
print("Key length:", len(api_key) if api_key else 0)

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

print(df.head())
print(calculate_total_sales())
print(get_best_selling_product())
print(get_sales_by_category("Electronics"))