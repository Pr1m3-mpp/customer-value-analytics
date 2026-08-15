import pandas as pd

path = "data/processed/customer_rfm.csv"
rfm = pd.read_csv(path)

r_med = rfm["Recency"].median()
f_med = rfm["Frequency"].median()
m_med = rfm["Monetary"].median()

def segment(row):
    if (
        row["Recency"] <= r_med
        and row["Frequency"] >= f_med
        and row["Monetary"] >= m_med
    ):
        return "Champions"

    elif (
        row["Recency"] > r_med
        and row["Monetary"] >= m_med
    ):
        return "At Risk"

    elif row["Frequency"] >= f_med:
        return "Loyal Customers"

    else:
        return "Others"

rfm["Segment"] = rfm.apply(segment, axis=1)

rfm.to_csv(path, index=False)

print("R median:", r_med)
print("F median:", f_med)
print("M median:", m_med)

print("\nSegment counts:")
print(rfm["Segment"].value_counts())

print("\nSaved:", path)