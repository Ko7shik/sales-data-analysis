import pandas as pd
import sqlite3

# Load CSV data
df = pd.read_csv("sales_data.csv")

# Create SQLite database in memory
conn = sqlite3.connect(":memory:")

# Load dataframe into SQL table
df.to_sql("sales_data", conn, index=False, if_exists="replace")

# Query 1: View all data
query1 = """
SELECT *
FROM sales_data;
"""
print("ALL DATA:")
print(pd.read_sql(query1, conn))

# Query 2: Total amount per order
query2 = """
SELECT
    order_id,
    product,
    quantity,
    price,
    quantity * price AS total_amount
FROM sales_data;
"""
print("\nTOTAL AMOUNT PER ORDER:")
print(pd.read_sql(query2, conn))

# Query 3: Revenue by category
query3 = """
SELECT
    category,
    SUM(quantity * price) AS total_revenue
FROM sales_data
GROUP BY category;
"""
print("\nREVENUE BY CATEGORY:")
print(pd.read_sql(query3, conn))

# Query 4: Product revenue ranking
query4 = """
SELECT
    product,
    SUM(quantity * price) AS product_revenue
FROM sales_data
GROUP BY product
ORDER BY product_revenue DESC;
"""
print("\nPRODUCT REVENUE:")
print(pd.read_sql(query4, conn))

conn.close()