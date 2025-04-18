-- Step 1: Create the customers table by combining data from multiple tables
DO $$
DECLARE
    table_name TEXT;
    sql_query TEXT := 'CREATE TABLE customers AS ';
    first_table BOOLEAN := TRUE;
BEGIN
    FOR table_name IN
        SELECT t.table_name
        FROM information_schema.tables t
        WHERE t.table_name LIKE 'data_202%_%%%' ESCAPE '\'
          AND t.table_schema = 'public'
    LOOP
        RAISE NOTICE 'Processing table: %', table_name;
        IF first_table THEN
            sql_query := sql_query || 'SELECT * FROM ' || table_name;
            first_table := FALSE;
        ELSE
            sql_query := sql_query || ' UNION ALL SELECT * FROM ' || table_name;
        END IF;
    END LOOP;
    EXECUTE sql_query;
END $$;

-- Step 2: Clean the items table
ALTER TABLE items RENAME TO items_backup;

CREATE TABLE items (
    product_id INT,
    category_id BIGINT,
    category_code VARCHAR(255),
    brand VARCHAR(255)
);

INSERT INTO items (product_id, category_id, category_code, brand)
SELECT 
    product_id,
    MAX(category_id) AS category_id,
    MAX(category_code) AS category_code,
    MAX(brand) AS brand
FROM items_backup
GROUP BY product_id;

DROP TABLE items_backup;

-- Step 3: Remove duplicates from the customers table
CREATE TABLE customers_temp AS
SELECT event_time, event_type, product_id, price, user_id, user_session
FROM (
    SELECT * ,
           ROW_NUMBER() OVER (
               PARTITION BY event_type, product_id, price, user_id, user_session
               ORDER BY event_time
           ) AS rn,
           LAG(event_time) OVER (
               PARTITION BY event_type, product_id, price, user_id, user_session
               ORDER BY event_time
           ) AS prev_event_time
    FROM customers
) subquery
WHERE rn = 1
  OR event_time > prev_event_time + INTERVAL '1 second';

-- Replace the old customers table with the new one
DROP TABLE customers;
ALTER TABLE customers_temp RENAME TO customers;

-- Step 4: Join the customers and items tables
CREATE TABLE customers_temp AS
SELECT *
FROM 
    customers c
LEFT JOIN 
    items i
USING (product_id);

-- Replace the old customers table with the joined one
DROP TABLE customers;
ALTER TABLE customers_temp RENAME TO customers;