import numpy as np
import pandas as pd

np.random.seed(42)

dates = pd.date_range(start="2025-01-01", periods=100, freq="D")
products = ["Spectacle Frame", "Blue Light Glasses", "Lens Case"]

data = []

for product in products:
    base_sales = np.random.randint(20, 50)
    for date in dates:
        noise = np.random.randint(-5, 10)
        sales = max(5, base_sales + noise)
        inventory_level = np.random.randint(10, 100)

        data.append(
            {
                "Date": date,
                "Product": product,
                "Sales": sales,
                "Stock_Level": inventory_level,
            }
        )

df = pd.DataFrame(data)
df.to_csv("sales_data.csv", index=False)
print("✅ New sales_data.csv generated!")