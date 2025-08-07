# 🛍️ E-Commerce Data Engineering Pipeline

This is a full-stack data engineering portfolio project simulating an e-commerce platform's analytics pipeline.

## 🏗️ Tech Stack

- Python
- DuckDB (OLAP)
- Pandas
- Streamlit (Dashboard)
- Subprocess (Basic orchestration)

## 🧱 Pipeline Architecture

1. **Ingestion** – Generate 1000 fake orders with Faker
2. **Batch Processing** – Aggregate revenue by category
3. **Modeling** – Create star schema using DuckDB
4. **Orchestration** – Simple controller to run all steps
5. **Analytics** – Streamlit dashboard for insights

## 📁 Folder Structure