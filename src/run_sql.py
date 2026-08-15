# import duckdb

# con = duckdb.connect()

# with open("sql/01_clean_transactions.sql", "r", encoding="utf-8") as f:
#     query = f.read()

# result = con.execute(query).df()

# print(result.shape)
# print(result.head())

# con.close()


# import duckdb

# con = duckdb.connect()

# with open("sql/02_customer_rfm.sql", "r", encoding="utf-8") as f:
#     query = f.read()

# rfm = con.execute(query).df()

# rfm.to_csv("data/processed/customer_rfm.csv", index=False)

# print(rfm.shape)
# print(rfm.head())
# print("Saved: data/processed/customer_rfm.csv")

# con.close()


import duckdb

con = duckdb.connect()

with open("sql/03_customer_kpis.sql", "r", encoding="utf-8") as f:
    query = f.read()

kpis = con.execute(query).df()

kpis.to_csv("data/processed/customer_kpis.csv", index=False)

print(kpis)
print("Saved: data/processed/customer_kpis.csv")

con.close()