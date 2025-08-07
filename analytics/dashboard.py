import streamlit as st
import duckdb
import pandas as pd 

# Connect to DuckDB
con = duckdb.connect("ur-ecommerce.duckdb")

st.title("📊 E-Commerce Analytics Dashboard")

# Revenue by Category
st.header("💰 Revenue by Category")
df_cat = con.execute("""
    SELECT category, SUM(price) AS total_revenue
    FROM fact_orders
    GROUP BY category
    ORDER BY total_revenue DESC
""").df()
st.bar_chart(df_cat.set_index("category"))

# Orders per Weekday
st.header("📆 Orders by Weekday")
df_time = con.execute("""
    SELECT t.weekday, COUNT(*) AS num_orders
    FROM fact_orders f
    JOIN dim_time t ON f.timestamp = t.timestamp
    GROUP BY t.weekday
    ORDER BY t.weekday
""").df()
st.line_chart(df_time.set_index("weekday"))