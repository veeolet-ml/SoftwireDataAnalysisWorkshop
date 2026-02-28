import pandas as pd
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

def clean_data(file_path):
    df = pd.read_csv(file_path)

    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

    df["date"] = pd.to_datetime(df["date"], errors="coerce", dayfirst=True)
    
    failed_dates = df["date"].isna().sum()
    print(f"Failed to parse {failed_dates} dates.")

    df["amount"] = df["amount"].str.replace("$", "").str.replace(",", "").astype(float, errors="raise")
    failed_amounts = df["amount"].isna().sum()
    print(f"Failed to parse {failed_amounts} amounts.")

    df["boxes_shipped"] = df["boxes_shipped"].astype(int, errors="raise")
    failed_boxes = df["boxes_shipped"].isna().sum()
    print(f"Failed to parse {failed_boxes} boxes shipped.")

    df.dropna(subset=["amount"], inplace=True)

    print(df.isna().sum())
    df.drop_duplicates(inplace=True)
    df.info()
    df.describe()

    output_path = ROOT_DIR / "data/processed/chocolate_sales_clean.csv"
    df.to_csv(output_path, index=False)

if __name__ == "__main__":
    file_path = ROOT_DIR / "data/raw/chocolate_sales_raw.csv"
    clean_data(file_path)
