WITH transactions AS (
    SELECT *
    FROM read_csv_auto('data/processed/clean_transactions.csv')
),

snapshot AS (
    SELECT MAX(InvoiceDate)::DATE + INTERVAL 1 DAY AS snapshot_date
    FROM transactions
)

SELECT
    CustomerID,
    date_diff(
        'day',
        MAX(InvoiceDate)::DATE,
        snapshot_date::DATE
    ) AS Recency,
    COUNT(DISTINCT InvoiceNo) AS Frequency,
    ROUND(SUM(Revenue), 2) AS Monetary

FROM transactions
CROSS JOIN snapshot

GROUP BY
    CustomerID,
    snapshot_date

ORDER BY
    Monetary DESC;