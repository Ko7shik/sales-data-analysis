-- View all sales data
SELECT *
FROM sales_data;
-- Calculate total amount per order
SELECT
    order_id,
    product,
    quantity,
    price,
    quantity * price AS total_amount
FROM sales_data;
-- Total revenue by category
SELECT
    category,
    SUM(quantity * price) AS total_revenue
FROM sales_data
GROUP BY category;
-- Top selling products by revenue
SELECT
    product,
    SUM(quantity * price) AS product_revenue
FROM sales_data
GROUP BY product
ORDER BY product_revenue DESC;