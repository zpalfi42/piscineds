ALTER TABLE customers RENAME TO customers_backup_2;

CREATE TABLE customers AS
SELECT *
FROM 
    customers_backup_2 c
LEFT JOIN 
    items i
USING (product_id); 