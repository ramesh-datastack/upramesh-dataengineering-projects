import duckdb
import os
import pandas as pd

#load your raw order data
input_file = "../data/raw/orders.csv"
df = pd.read_csv(input_file)

# Open (or create) a DuckDB database file
con = duckdb.connect('ur-ecommerce.duckdb')
con.execute("DROP TABLE IF EXISTS fact_orders")
con.execute("CREATE TABLE fact_orders AS SELECT * FROM df")

# Create time dimension from timestamp
con.execute("""
    CREATE OR REPLACE TABLE dim_time AS
    SELECT
        DISTINCT timestamp,
        strftime(CAST(timestamp AS TIMESTAMP), '%Y-%m-%d') AS date,
        strftime(CAST(timestamp AS TIMESTAMP), '%Y') AS year,
        strftime(CAST(timestamp AS TIMESTAMP), '%m') AS month,
        strftime(CAST(timestamp AS TIMESTAMP), '%w') AS weekday
    FROM fact_orders
""")

# Create product dimension (dummy enrichment)
con.execute("""
    CREATE OR REPLACE TABLE dim_products AS
    SELECT DISTINCT
        productId as product_id,
        category,
        'Brand_' || (product_id % 5) AS brand
    FROM fact_orders
""")

print("✅ Star schema created in ecommerce.duckdb")