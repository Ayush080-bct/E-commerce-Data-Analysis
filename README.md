# E-commerce Data Analysis

## Overview
This project analyzes real-world e-commerce transaction data using Python.
The goal is to understand customer purchasing behavior, identify key revenue drivers,
and segment customers using RFM analysis for business decision-making.

---

## Dataset
- Kaggle E-commerce Dataset
- Transaction-level retail data containing purchases and returns
- Time period: 2010–2011

---

## Tools & Libraries
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn

---

## Phase 1: Data Cleaning & Preprocessing
- Loaded raw transactional data
- Handled text encoding issues
- Removed rows with missing `CustomerID`
- Converted `InvoiceDate` to datetime format
- Created `TotalPrice` feature (`Quantity × UnitPrice`)
- Identified cancelled transactions using negative quantities and invoice prefixes

---

## Phase 2: Exploratory Data Analysis (EDA)

### Top Products by Revenue
- *Regency CakeStand 3 Tier* generates the highest total revenue.
- Indicates strong demand and/or higher unit price.
- Can be prioritized for inventory planning and promotions.

### Revenue by Country
- The United Kingdom contributes the majority of total revenue.
- Other countries contribute significantly less in comparison.
- Indicates strong market dependence on the UK region.

### Top Customers by Revenue
- A small number of customers generate a large portion of total revenue.
- High-value customers are mostly located in the United Kingdom.
- Enables targeted loyalty and retention strategies.

### Revenue Trend Over Time
- Revenue increases from July to November, peaking in November.
- Indicates strong seasonal demand.
- Inventory and supply planning should focus on this period.

### Quantity & Transaction Behavior
- Most transactions involve small positive quantities.
- Negative quantities indicate returns or cancelled orders.
- Returns exist but form a small portion of overall transactions.

### Transaction Value Distribution
- Most transactions fall within low to mid price ranges.
- Distribution is right-skewed with a few high-value outliers.
- Confirms high-volume, low-price business behavior.

---

## Phase 3: RFM Analysis & Customer Segmentation

### RFM Feature Engineering
Customers were analyzed using:
- **Recency** – Days since last purchase
- **Frequency** – Number of unique invoices
- **Monetary** – Total revenue per customer

RFM metrics were calculated at the customer level.

---

### RFM Scoring
- R, F, and M values were converted into quantile-based scores
- Higher scores represent more valuable customers
- Normalization allows fair comparison across customer groups

---

### Customer Segmentation
Customers were segmented using custom business logic implemented in `segmentFunc.py`.

**Segments include:**
- Champions
- Loyal Customers
- Potential Loyalists
- At Risk Customers
- Hibernating / Lost Customers

Segmentation is based on combined RFM score patterns.

---

### Purchase & Return Behavior
- Returns identified using negative quantities and cancelled invoices
- Customers with full purchase–return cancellations were retained for behavioral analysis
- Enables detection of high-return or abnormal purchasing behavior

---

### Visualization Insights
- Frequency vs Monetary scatter plot created
- Recency used as color encoding
- Reveals:
  - High-value loyal customers
  - Frequent small-purchase customers
  - Inactive or declining customers

---

### Phase 4: Customer Clustering (Unsupervised Learning)
- Standardize RFM features
- Determine optimal clusters using Elbow Method
- Apply KMeans clustering
- Profile clusters and validate against rule-based segments

--- 

## Key Business Insights
- Revenue is driven by a small group of high-value customers
- Recent customers often start with low monetary value
- Frequent small purchases can accumulate high lifetime value
- Returns do not dominate overall business behavior

---

## Project Status
- ✅ Data Cleaning
- ✅ Exploratory Data Analysis
- ✅ RFM Modeling
- ✅ Customer Segmentation
- ✅ Visualization & Interpretation

---

## Future Improvements
- Return-heavy customer risk analysis
- Churn prediction modeling
- Advanced clustering (DBSCAN / Hierarchical)
- Interactive dashboard for business users