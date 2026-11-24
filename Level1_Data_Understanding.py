import pandas as pd

# Load Dataset
df = pd.read_csv("Big_Mart_Sales.csv")

print("=== 1. DATASET INFO ===")
df.info()

print("\n=== 2. MISSING VALUES COUNT ===")
print(df.isnull().sum())

print("\n=== 3. ITEM_FAT_CONTENT DISTRIBUTION ===")
print(df["Item_Fat_Content"].value_counts())

print("\n=== 4. ZERO VISIBILITY COUNT ===")
print("Zero Visibility Items:", (df["Item_Visibility"] == 0).sum())

print("\n=== 5. SUMMARY STATISTICS ===")
print(df.describe())

print("\n=== 6. DUPLICATE ROWS ===")
print("Duplicate rows:", df.duplicated().sum())

print("\n=== 7. COLUMNS ===")
print(df.columns.tolist())