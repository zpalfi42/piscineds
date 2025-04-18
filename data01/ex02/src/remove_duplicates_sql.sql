ALTER TABLE customers RENAME TO customers_backup;

CREATE TABLE customers AS
SELECT event_time, event_type, product_id, price, user_id, user_session
FROM (
    SELECT *,
           ROW_NUMBER() OVER (
               PARTITION BY event_type, product_id, price, user_id, user_session
               ORDER BY event_time
           ) AS rn,
           LAG(event_time) OVER (
               PARTITION BY event_type, product_id, price, user_id, user_session
               ORDER BY event_time
           ) AS prev_event_time
    FROM customers_backup
) subquery
WHERE rn = 1
  OR event_time > prev_event_time + INTERVAL '1 second';