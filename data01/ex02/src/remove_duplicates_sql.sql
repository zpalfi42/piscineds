CREATE TEMP table temp_customers AS
SELECT *
FROM (
    SELECT *,
           ROW_NUMBER() OVER (PARTITION BY event_type, product_id, price, user_id, user_session ORDER BY event_time) AS rn
    FROM customers
) subquery
WHERE rn = 1;
\echo 'truncating customers';
TRUNCATE TABLE customers;
\echo 'Inserting into customers';
INSERT INTO customers
SELECT event_time, event_type, product_id, price, user_id, user_session
FROM temp_customers;
\echo 'Dropping temp table';
DROP TABLE temp_customers;