# Exploratory Data Analysis – Retail Sales

## 1. Project overview
This project explores a **synthetic retail sales dataset** created for learning and portfolio practice. It contains 1,200 order records across 2025. The data is not a real company's transaction data.

## 2. Dataset overview
- Rows: 1,200
- Columns: 15
- Period: 1 January 2025 to 31 December 2025 (sampled order dates)
- Currency: Indian Rupees (INR)
- Missing values: 0
- Duplicate Order_ID values: 0

## 3. Key statistics
- Total sales: ₹14,049,247.37
- Total profit: ₹3,943,614.93
- Average order sales: ₹11,707.71
- Average customer rating: 3.96/5
- Return rate: 6.75%

## 4. Useful insights
1. **Category performance:** Electronics generated the highest total sales (₹6,966,630), making it the strongest category by revenue.
2. **Regional performance:** North recorded the highest sales (₹4,186,711) among the four regions.
3. **Sales channel:** Online contributed the most revenue (₹8,062,903); compare channel-level order counts and average order value before changing channel strategy.
4. **Seasonality:** 2025-12 was the strongest month by sales, while 2025-05 was the weakest. Monthly patterns can help with inventory and campaign planning.
5. **Returns:** 6.8% of orders are marked as returned. This should be monitored by category and region to identify potential quality or fulfilment issues.
6. **Customer experience:** Average customer rating is 3.96/5. Review ratings alongside returns and category to find improvement opportunities.
7. **Outliers:** The sales boxplot highlights unusually large orders. Five records were intentionally made unusually high in the generated practice dataset; validate them before treating them as normal demand.

## 5. Charts
1. Orders by product category
2. Monthly sales trend
3. Sales by region
4. Sales by channel
5. Sales distribution by category (boxplot)
6. Correlation heatmap

## 6. Recommendations
- Prioritise inventory planning for high-revenue categories and regions.
- Compare online and store channels using both revenue and average order value.
- Investigate categories/regions with higher return rates before making operational changes.
- Plan promotions and stock levels around observed monthly sales patterns.
- Validate unusually high sales records to rule out data-entry or measurement issues.

## 7. Limitations
The dataset is synthetic and contains deliberately inserted high-sales outliers for anomaly-detection practice. Findings demonstrate an EDA workflow and should not be presented as real-world company facts.
