# ==========================================
# LEVEL 2: DATA CLEANING & PREPROCESSING
# Project: Sysslan Analytics (Big Mart Sales)
# ==========================================

# ==========================================
# LEVEL 2: DATA CLEANING & PREPROCESSING
# Project: Sysslan Analytics (Big Mart Sales)
# ==========================================

import pandas as pd
import numpy as np

# 1. Dataset Load
df = pd.read_csv("Big_Mart_Sales.csv")
print("--- Data Cleaning Shuru Ho Rahi Hai ---")

# 2. Item_Fat_Content Fix & Non-Edible Mark
df['Item_Fat_Content'] = df['Item_Fat_Content'].replace({
    'LF': 'Low Fat',
    'low fat': 'Low Fat',
    'reg': 'Regular'
})
# Non-Edible category mapping (Non-Consumable items)
df.loc[df['Item_Identifier'].str.startswith('NC'), 'Item_Fat_Content'] = 'Non-Edible'

print("\n1. Fixed Item_Fat_Content Distribution:")
print(df['Item_Fat_Content'].value_counts())

# 3. Missing Value Imputation
# Item_Weight
item_weight_mean = df.groupby('Item_Identifier')['Item_Weight'].transform('mean')
df['Item_Weight'] = df['Item_Weight'].fillna(item_weight_mean)
df['Item_Weight'] = df['Item_Weight'].fillna(df['Item_Weight'].mean())

# Outlet_Size
outlet_size_mode = df.groupby('Outlet_Type')['Outlet_Size'].agg(lambda x: x.mode()[0] if not x.mode().empty else 'Medium')
df['Outlet_Size'] = df['Outlet_Size'].fillna(df['Outlet_Type'].map(outlet_size_mode))

# 4. Item_Visibility Clean (Replace 0 with Group Mean)
df['Item_Visibility'] = df['Item_Visibility'].replace(0, np.nan)
item_vis_mean = df.groupby('Item_Identifier')['Item_Visibility'].transform('mean')
df['Item_Visibility'] = df['Item_Visibility'].fillna(item_vis_mean)
df['Item_Visibility'] = df['Item_Visibility'].fillna(df['Item_Visibility'].mean())

print("\n2. Missing Values After Cleaning (Should be 0 across all 11 columns):")
print(df.isnull().sum())

# 5. Export Dataset with all 11 Columns
df.to_csv("Big_Mart_Sales_Cleaned.csv", index=False)
print("\n--- SUCCESS: Cleaned data with all 11 columns saved as 'Big_Mart_Sales_Cleaned.csv' ---")