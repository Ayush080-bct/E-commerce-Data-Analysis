# E-commerce Data Analysis (Work in Progress)

## Overview
This project analyzes real-world e-commerce transaction data using Python and Pandas.
Currently focused on data cleaning and preprocessing.

## Dataset
- Kaggle E-commerce dataset
- Transaction-level retail data

## Current Progress
- Loaded raw data
- Handled text encoding
- Removed missing CustomerID values
- Converted InvoiceDate to datetime

## Tools
- Python
- Pandas
- NumPy
- Matplotlib
- seaborn

## Phase 2: Exploratory Data Analysis (EDA) Insights

### Top Products by Revenue
- *Regency CakeStand 3 Tier* generates the highest total revenue.
- Indicates strong demand and/or higher unit price.
- Could be prioritized for inventory planning and promotions.

### Revenue by Country
- The United Kingdom contributes the majority of total revenue.
- Combined revenue from other countries is significantly lower than that of the UK.
- Opportunity to grow revenue by expanding sales and marketing efforts in international markets.
- Due to high demand, inventory and supply planning should prioritize the UK market.

### Top Customers by Revenue
- Customers `14646` and `18102` generate the highest total revenue.
- Several other customers also contribute significantly, showing that a small group drives most sales.
- Most top-spending customers are located in the United Kingdom, reflecting the market concentration.
- Insights can guide targeted promotions and loyalty programs.

### Total Customers by Country
- The United Kingdom has the highest number of customers: 361,878.
- Germany, France, and EIRE follow, but with far fewer customers: 9,495; 8,491; and 7,485 respectively.
- Other countries like Spain (2,533), Netherlands (2,371), Belgium (2,069), Switzerland (1,877), Portugal (1,480), Australia (1,259), Norway (1,086), and Italy (803) contribute relatively smaller customer bases.
- This shows a **high concentration of customers in the UK**, indicating that the business relies heavily on this market.
- There is potential to **grow the customer base in other countries** through targeted marketing and expansion strategies.

### Revenue Trend Over Time
- From **July to November**, revenue steadily rose, peaking in November.
- This indicates **high seasonal demand** during these months.
- Supply and inventory planning should be prioritized in this period to meet demand efficiently.

### TotalPrice Distribution (Box Plot)
- The majority of transactions fall within a low to moderate TotalPrice range.
- The distribution is right-skewed with several high-value outliers.
- Negative TotalPrice values indicate returns or cancelled transactions.

### Transaction Value Insights
- The middle 50% of transactions fall approximately between $5 and $18, indicating typical purchase values.
- Higher-value transactions extend up to around $38, representing the upper spending range.
- Negative TotalPrice values (−1 to −18) indicate returned or cancelled orders.
- Low-value purchases ($0–$4) are also common, suggesting frequent small-item transactions.

### Overall Quantity Distribution
- Most transactions have positive quantities, indicating successful sales.
- Returns (negative quantities) are present but form a very small portion of the data.
- Large return quantities are rare, suggesting returns have minimal impact on overall sale.
- X-axis represents the quantity of items per transaction.
- Y-axis represents the frequency of transactions.
- Most transactions involve small positive quantities, while returns are infrequent.


### The business operates on high-volume, low-price sales with occasional bulk orders.Returns exist but do not dominate transaction behavior.

## Next Steps
- Customer segmentation using RFM analysis and clustering.  
- Predictive analysis for marketing and inventory planning.  
- Feature engineering for potential ML models.  
