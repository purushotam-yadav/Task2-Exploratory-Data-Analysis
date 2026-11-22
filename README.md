# Task 2 – Exploratory Data Analysis (EDA)

## Project
Retail Sales Exploratory Data Analysis using Python.

> Dataset note: `retail_sales_eda_dataset.csv` is a synthetic practice dataset generated for this project. It is not actual company/customer data. A few unusually high sales values are intentionally included for outlier analysis.

## Tools
- Python
- Pandas
- NumPy
- Matplotlib

## Setup
```bash
pip install -r requirements.txt
```

## Run
Open the project folder in VS Code, open the terminal, and run:
```bash
python src/eda_analysis.py
```

The script prints dataset summaries, grouped analysis, monthly sales and correlations. Charts are included in `charts/`.

## Project structure
- `data/` – dataset CSV
- `src/` – reusable Python EDA script
- `charts/` – generated visualisations
- `reports/` – written EDA report

## Main analysis
- Dataset shape, data types, missing values and duplicates
- Descriptive statistics
- Category, region and channel analysis
- Monthly sales trend
- Correlation and outlier exploration
- Seven insight statements and business recommendations
