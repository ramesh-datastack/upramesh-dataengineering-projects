# generate_orders.py
from faker import Faker
import os
import random
import csv
from datetime import datetime

fake = Faker()

output_dir = "../data/raw/"
os.makedirs(output_dir, exist_ok=True)

output_file = "../data/raw/orders.csv"

def generate_orders():
    return{
        "orderId": fake.uuid4(),
        "userId": fake.uuid4(),
        "productId": random.randint(1000,2000),
        "category": random.choice(["Electronics","Books","Clothing","Home","Toys"]),
        "price": round(random.uniform(10.0,500.0),2),
        "timestamp": datetime.utcnow().isoformat()
    }

with open(output_file, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["orderId", "userId", "productId","category","price","timestamp"])
    writer.writeheader()
    for _ in range(1000): # generate 1000 fake orders
        writer.writerow(generate_orders())

print(f"generated 1000 fake orders at {output_file}")