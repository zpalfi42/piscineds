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