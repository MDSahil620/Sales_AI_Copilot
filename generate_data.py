import pandas as pd
import numpy as np

# Sample Sales Data Generate karna
np.random.seed(42)
dates = pd.date_range(start="2025-01-01", periods=100, freq="D")
products = ["Spectacle Frame", "Blue Light Glasses", "Lens Case"]

data = []
for date in dates:
    prod = np.random.choice(products)
    units_sold = np.random.randint(5, 50)
    price = 300 if prod == "Spectacle Frame" else (400 if prod == "Blue Light Glasses" else 100)
    revenue = units_sold * price
    data.append([date, prod, units_sold, price, revenue])

df = pd.DataFrame(data, columns=["Date", "Product", "Units_Sold", "Price", "Revenue"])
df.to_csv("sales_data.csv", index=False)
print("SUCCESS: sales_data.csv file ban gayi hai!")