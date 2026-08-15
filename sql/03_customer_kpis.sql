WITH transactions AS (
    SELECT *
    FROM read_csv_auto('data/processed/clean_transactions.csv')
),

customer_orders AS (
    SELECT
        CustomerID,
        COUNT(DISTINCT InvoiceNo) AS order_count
    FROM transactions
    GROUP BY CustomerID
)

SELECT
    COUNT(DISTINCT CustomerID) AS Customers,
    COUNT(DISTINCT InvoiceNo) AS Orders,
    ROUND(SUM(Revenue), 2) AS Revenue,
    ROUND(SUM(Revenue) / COUNT(DISTINCT InvoiceNo), 2) AS AOV,
    (
        SELECT COUNT(*)
        FROM customer_orders
        WHERE order_count > 1
    ) AS RepeatCustomers,
    ROUND(
        100.0 * (
            SELECT COUNT(*)
            FROM customer_orders
            WHERE order_count > 1
        ) / COUNT(DISTINCT CustomerID),
        2
    ) AS RepeatPurchaseRate
FROM transactions;