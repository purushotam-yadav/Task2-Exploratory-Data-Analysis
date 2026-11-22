"""
Exploratory Data Analysis – Retail Sales
Run from project root: python src/eda_analysis.py
"""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "retail_sales_eda_dataset.csv"
CHARTS = ROOT / "charts"
CHARTS.mkdir(exist_ok=True)

df = pd.read_csv(DATA)
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

print("\n--- DATASET OVERVIEW ---")
print(df.head())
print("\nShape:", df.shape)
print("\nData types:\n", df.dtypes)
print("\nMissing values:\n", df.isnull().sum())
print("\nDuplicate rows:", df.duplicated().sum())
print("\n--- NUMERICAL SUMMARY ---")
print(df.describe().round(2))

print("\n--- CATEGORY SUMMARY ---")
print(df.groupby("Category").agg(
    Orders=("Order_ID", "count"),
    Total_Sales=("Sales_INR", "sum"),
    Average_Sales=("Sales_INR", "mean"),
    Total_Profit=("Profit_INR", "sum")
).round(2).sort_values("Total_Sales", ascending=False))

print("\n--- REGION SUMMARY ---")
print(df.groupby("Region")["Sales_INR"].agg(["count", "sum", "mean"]).round(2))

print("\n--- MONTHLY SALES ---")
monthly = df.set_index("Order_Date").resample("ME")["Sales_INR"].sum()
print(monthly.round(2))

print("\n--- CORRELATION ---")
print(df.select_dtypes("number").corr().round(2))

# Recreate charts
plots = [
    ("Category", "01_orders_by_category.png", "Orders by Product Category", "Category", "Orders"),
]
for col, filename, title, xlabel, ylabel in plots:
    plt.figure(figsize=(9, 5))
    df[col].value_counts().plot(kind="bar")
    plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel)
    plt.tight_layout(); plt.savefig(CHARTS / filename, dpi=150); plt.close()

monthly = df.assign(Month=df["Order_Date"].dt.to_period("M").astype(str)).groupby("Month")["Sales_INR"].sum()
plt.figure(figsize=(10,5)); monthly.plot(marker="o")
plt.title("Monthly Sales Trend"); plt.xlabel("Month"); plt.ylabel("Sales (INR)")
plt.xticks(rotation=45); plt.tight_layout()
plt.savefig(CHARTS / "02_monthly_sales_trend.png", dpi=150); plt.close()

for col, filename, title in [
    ("Region", "03_sales_by_region.png", "Sales by Region"),
    ("Sales_Channel", "04_sales_by_channel.png", "Sales by Channel")
]:
    plt.figure(figsize=(8,5)); df.groupby(col)["Sales_INR"].sum().plot(kind="bar")
    plt.title(title); plt.xlabel(col); plt.ylabel("Sales (INR)")
    plt.tight_layout(); plt.savefig(CHARTS / filename, dpi=150); plt.close()

plt.figure(figsize=(8,5)); df.boxplot(column="Sales_INR", by="Category", rot=15)
plt.title("Sales Distribution by Category"); plt.suptitle("")
plt.xlabel("Category"); plt.ylabel("Sales (INR)")
plt.tight_layout(); plt.savefig(CHARTS / "05_sales_distribution_boxplot.png", dpi=150); plt.close()

numeric = df[["Unit_Price_INR","Quantity","Discount","Sales_INR","Cost_INR","Profit_INR","Customer_Rating"]]
corr = numeric.corr()
plt.figure(figsize=(8,6)); plt.imshow(corr, aspect="auto")
plt.xticks(range(len(corr.columns)), corr.columns, rotation=45, ha="right")
plt.yticks(range(len(corr.columns)), corr.columns); plt.colorbar(label="Correlation")
plt.title("Correlation Heatmap"); plt.tight_layout()
plt.savefig(CHARTS / "06_correlation_heatmap.png", dpi=150); plt.close()

print("\nEDA completed. Charts saved in the charts/ folder.")
