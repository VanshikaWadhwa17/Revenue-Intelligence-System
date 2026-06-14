SELECT churn_label, COUNT(*) AS cnt
FROM customers_raw
GROUP BY churn_label;
