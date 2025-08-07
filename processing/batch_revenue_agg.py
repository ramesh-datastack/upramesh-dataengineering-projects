import pandas as pd 
import os

# Paths
input_file = "../data/raw/orders.csv"
output_dir ="../data/processed/"
os.makedirs(output_dir, exist_ok=True)
output_file = os.path.join(output_dir, "revenue_by_category.csv")

#load data
try:
    print("Reading input CSV...")
    df = pd.read_csv(input_file)

    #group by category and sum revenue

    agg_df = df.groupby("category")["price"].sum().reset_index()
    agg_df.rename(columns={"price":"total_revenue"}, inplace=True)

    #save processed data
    agg_df.to_csv(output_file, index=False)
    print(f'Revenue by category saved to {output_file}')
    print(agg_df)
except Exception as e:
    print(f"❌ Error: {e}")