import subprocess

print("🚀 Starting E-commerce Data Pipeline")

# Step 1: Generate raw orders
print("📦 Generating orders...")
subprocess.run(["python", "ingestion/generate_orders.py"], check=True)

# Step 2: Run batch processing job
print("🧮 Processing revenue aggregates...")
subprocess.run(["python", "processing/batch_revenue_agg.py"], check=True)

# Step 3: Create star schema in DuckDB
print("🧱 Creating star schema...")
subprocess.run(["python", "processing/modeling/create_star_schema.py"], check=True)

print("✅ Pipeline completed successfully!")