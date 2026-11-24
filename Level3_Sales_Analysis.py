# ==========================================
# LEVEL 3: SALES & EXPLORATORY DATA ANALYSIS (EDA)
# Project: Sysslan Analytics (Big Mart Sales)
# ==========================================

import pandas as pd

# 1. Cleaned Dataset Load
df = pd.read_csv("Big_Mart_Sales_Cleaned.csv")
 
 
print("--- Level 3: Exploratory Data Analysis Start ---")

# ---------------------------------------------------------
# Step 1: Total Sales
# ---------------------------------------------------------
Total_sales = df['Item_MRP'].sum()
print("Total Sales Value:", round(Total_sales))
print("Average MRP:", round(df['Item_MRP'].mean(), 2))

# ---------------------------------------------------------
# Task 1: Category Wise Pricing & Volume Analysis
# ---------------------------------------------------------
print("\n=== 1. TOP ITEM TYPES BY TOTAL MRP VALUE ===")
category_summary = df.groupby('Item_Type')['Item_MRP'].agg(['count', 'mean', 'sum']).reset_index()
category_summary.columns = ['Item_Type', 'Product_Count', 'Avg_MRP', 'Total_MRP_Value']
category_summary = category_summary.sort_values(by='Total_MRP_Value', ascending=False)
print(category_summary.head(10))

# ---------------------------------------------------------
# Task 2: Outlet Type & Location Performance
# ---------------------------------------------------------
print("\n=== 2. OUTLET TYPE PERFORMANCE ===")
outlet_type_summary = df.groupby('Outlet_Type')['Item_MRP'].agg(['count', 'mean', 'sum']).reset_index()
outlet_type_summary.columns = ['Outlet_Type', 'Product_Count', 'Avg_MRP', 'Total_MRP_Value']
print(outlet_type_summary)

print("\n=== 3. OUTLET LOCATION TIER PERFORMANCE ===")
location_summary = df.groupby('Outlet_Location_Type')['Item_MRP'].agg(['count', 'mean', 'sum']).reset_index()
location_summary.columns = ['Location_Tier', 'Product_Count', 'Avg_MRP', 'Total_MRP_Value']
print(location_summary)

# ---------------------------------------------------------
# Task 3: Item Fat Content Comparison
# ---------------------------------------------------------
print("\n=== 4. FAT CONTENT DISTRIBUTION & PRICING ===")
fat_summary = df.groupby('Item_Fat_Content')['Item_MRP'].agg(['count', 'mean', 'sum']).reset_index()
fat_summary.columns = ['Fat_Content', 'Product_Count', 'Avg_MRP', 'Total_MRP_Value']
print(fat_summary)

# ---------------------------------------------------------
# Task 4: Store Age Calculation & Analysis
# ---------------------------------------------------------
# Current year 2026 ke hisab se outlet ki age calculate karna
df['Outlet_Age'] = 2026 - df['Outlet_Establishment_Year']

print("\n=== 5. OUTLET AGE VS PRODUCT COUNT ===")
store_summary = df.groupby(['Outlet_Identifier', 'Outlet_Type', 'Outlet_Age'])['Item_MRP'].agg(['count', 'mean']).reset_index()
store_summary.columns = ['Outlet_ID', 'Outlet_Type', 'Outlet_Age_Years', 'Product_Count', 'Avg_MRP']
print(store_summary)

# Top 10 products by sales value
top10 = df.groupby('Item_Identifier')['Item_MRP'].sum().sort_values(ascending=False).head(10)
print("\n=== TOP 10 PRODUCTS BY SALES VALUE ===")
print(top10)
top10.to_csv("Level3_Top10_Products.csv")

# Sales by outlet
outlet_sales = df.groupby('Outlet_Identifier')['Item_MRP'].sum().sort_values(ascending=False)
print("\n=== SALES BY OUTLET ===")
print(outlet_sales)
outlet_sales.to_csv("Level3_Outlet_Sales.csv")

# ---------------------------------------------------------
# Task 5: Export Summary Findings
# ---------------------------------------------------------
category_summary.to_csv("Level3_Category_Summary.csv", index=False)
print("\n--- SUCCESS: Level 3 Analysis complete! Summary 'Level3_Category_Summary.csv' me save ho gayi hai. ---")