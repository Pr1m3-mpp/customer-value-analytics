# import pandas as pd

# file_path = "data/raw/Online Retail.xlsx"

# df = pd.read_excel(file_path)

# print(df.shape)
# print(df.columns.tolist())
# print(df.head())


# import pandas as pd

# file_path = "data/raw/Online Retail.xlsx"
# df = pd.read_excel(file_path)

# print("Shape:", df.shape)

# print("\nMissing values:")
# print(df.isna().sum())

# print("\nData types:")
# print(df.dtypes)

# print("\nCancelled rows:")
# print(df["InvoiceNo"].astype(str).str.startswith("C").sum())

# print("\nQuantity <= 0:")
# print((df["Quantity"] <= 0).sum())

# print("\nUnitPrice <= 0:")
# print((df["UnitPrice"] <= 0).sum())

# print("\nDate range:")
# print(df["InvoiceDate"].min(), "->", df["InvoiceDate"].max())


import pandas as pd

input_path = "data/raw/Online Retail.xlsx"
output_path = "data/processed/clean_transactions.csv"

df = pd.read_excel(input_path)

df = df[
    df["CustomerID"].notna()
    & (df["Quantity"] > 0)
    & (df["UnitPrice"] > 0)
    & (~df["InvoiceNo"].astype(str).str.startswith("C"))
].copy()

df["CustomerID"] = df["CustomerID"].astype(int)
df["Revenue"] = df["Quantity"] * df["UnitPrice"]

df = df[df["Revenue"] > 0]

df.to_csv(output_path, index=False)

print("Original rows:", 541909)
print("Clean rows:", len(df))
print("Saved:", output_path)