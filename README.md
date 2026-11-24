 # Big Mart Sales Analysis

A Data Analytics project focused on understanding product data, data cleaning, exploratory data analysis (EDA), and Power BI visualization using Python, Pandas, and Power BI.

## Project Overview

This project analyzes Big Mart product and outlet data to identify patterns in product categories, pricing, outlet types, location tiers, and product distribution.

The project is divided into five levels, covering data understanding, preprocessing, exploratory analysis, and dashboard visualization.

**Dataset:** 5,681 rows and 11 columns.

## Objectives

- Understand the dataset and identify data quality issues.
- Handle missing values and inconsistent categories.
- Perform exploratory data analysis using Python.
- Analyze product categories and outlet-level patterns.
- Create visualizations and dashboards using Power BI.

## Tools & Technologies

- Python
- Pandas
- NumPy
- Power BI
- CSV Dataset
- Data Cleaning
- Exploratory Data Analysis (EDA)
- Data Visualization

## Project Workflow

### Level 1 – Data Understanding

- Explored 5,681 rows and 11 columns.
- Identified missing values in `Item_Weight` and `Outlet_Size`.
- Found inconsistent labels in `Item_Fat_Content`.
- Identified 353 records with zero item visibility.
- Checked duplicate records and summary statistics.

### Level 2 – Data Cleaning

- Standardized `Item_Fat_Content` categories.
- Classified non-consumable products as `Non-Edible`.
- Imputed missing item weights using item-level mean values.
- Filled missing outlet sizes using outlet-type mode.
- Replaced zero visibility values using item-level mean values.
- Exported the cleaned dataset as `Big_Mart_Sales_Cleaned.csv`.

**Result:** No missing values remained in the cleaned dataset.

### Level 3 – Exploratory Data Analysis

Analyzed:

- Product category-wise pricing and product counts.
- Outlet type and location tier comparisons.
- Fat content distribution.
- Outlet age and product count.
- Top 10 products by MRP value.
- Outlet-wise MRP value.

Generated summary CSV files for further analysis.

### Level 4 – Power BI Visualization

Created Power BI visualizations using the analyzed data.

File: `Level4_Visualization.pbix`

### Level 5 – Power BI Dashboard & Insights

Created a Power BI dashboard to present the project analysis and insights.

File: `Level5_Dashboard_Insights.pbix`

## Key Findings

- Snack Foods had the highest total MRP value among product categories.
- Supermarket Type 1 had the highest product count and total MRP value among outlet types.
- Tier 3 outlets had the highest total MRP value among location tiers.
- Low Fat products represented the largest product group.
- The cleaned dataset contained zero missing values.

## Important Dataset Note

The provided dataset does not contain an `Item_Outlet_Sales` column. Therefore, this project uses `Item_MRP` for pricing and MRP-based comparisons. The calculated MRP totals should not be interpreted as actual sales revenue.

## Project Files

- `Big_Mart_Sales.csv` – Original dataset
- `Big_Mart_Sales_Cleaned.csv` – Cleaned dataset
- `Level1_Data_Understanding.py` – Data understanding
- `Level2_Data_Cleaning.py` – Data cleaning
- `Level3_Sales_Analysis.py` – Exploratory data analysis
- `Level1.Documentation.txt` – Level 1 report
- `Level2_Documentation.txt` – Level 2 report
- `Level3_Documentation.txt` – Level 3 report
- `Level3_Category_Summary.csv` – Category summary
- `Level3_Outlet_Sales.csv` – Outlet summary
- `Level3_Top10_Products.csv` – Top 10 products
- `Level4_Visualization.pbix` – Power BI visualization
- `Level5_Dashboard_Insights.pbix` – Power BI dashboard

## How to Run

1. Clone this repository:

   `git clone https://github.com/dipeshgunjal62940-svg/Big-Mart-Sales-Analysis.git`

2. Install the required libraries:

   `pip install pandas numpy`

3. Run the Python scripts in sequence:

   `python Level1_Data_Understanding.py`

   `python Level2_Data_Cleaning.py`

   `python Level3_Sales_Analysis.py`

4. Open the `.pbix` files using Microsoft Power BI Desktop.

## Author

**Dipesh Gunjal**

BCA Student | Aspiring Data Analyst

GitHub: [dipeshgunjal62940-svg](https://github.com/dipeshgunjal62940-svg)
