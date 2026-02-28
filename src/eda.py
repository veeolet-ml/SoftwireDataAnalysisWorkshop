import pandas as pd
from pathlib import Path
from matplotlib import pyplot as plt

ROOT_DIR = Path(__file__).resolve().parent.parent

if __name__ == "__main__":
    df = pd.read_csv(ROOT_DIR / "data/processed/chocolate_sales_clean.csv")
    print(df.head())
    print(df.describe())
    print(df.info())
    print(df.isna().sum().sort_values(ascending=False))

    # amount per month as bar chart
    df["date"] = pd.to_datetime(df["date"], yearfirst=True)
    df["month"] = df["date"].dt.month
    df["year"] = df["date"].dt.year
    plt.figure()
    df.groupby("month")["amount"].sum().plot(kind="bar")
    plt.title("Total Sales Amount per Month")
    plt.xlabel("Month")
    plt.ylabel("Total Sales Amount")
    plt.savefig(ROOT_DIR / "reports/figures/total_sales_amount_per_month.png")
    plt.close()

    # top 10 products by revenue as horizontal bar chart
    plt.figure()
    df.groupby("product")["amount"].sum().sort_values(ascending=False).head(10).plot(kind="barh")
    plt.title("Top 10 Products by Revenue")
    plt.xlabel("Total Sales Amount")
    plt.ylabel("Product")
    plt.savefig(ROOT_DIR / "reports/figures/top_10_products_by_revenue.png")
    plt.close()

    # boxes shipped vs revenue scatter plot
    plt.figure()
    plt.scatter(df["boxes_shipped"], df["amount"])
    plt.title("Boxes Shipped vs Revenue")
    plt.xlabel("Boxes Shipped")
    plt.ylabel("Revenue")
    plt.savefig(ROOT_DIR / "reports/figures/boxes_shipped_vs_revenue.png")
    plt.close()
