import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv("SeriesReport-20220828113454_1d0680.csv")

# Preview the data to identify header/footer rows and columns to clean
print(df.head(10))

# Drop unnecessary rows and columns (adjust as needed based on your file)
# For example, if the first few rows are metadata, skip them:
# df = pd.read_csv("SeriesReport-20220828113454_1d0680.csv", skiprows=4)

# If there are unnamed columns or columns not needed, drop them:
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

# Rename columns for clarity if needed (adjust as per your file)
# df.columns = ['Year', 'Month', 'Average_Price']

# Convert date or year column to datetime or int if needed
if 'Year' not in df.columns:
    # Try to extract year from a date column
    if 'Date' in df.columns:
        df['Year'] = pd.to_datetime(df['Date']).dt.year
    else:
        # If year is in another column, adjust accordingly
        pass

# Convert price column to numeric, handle errors
price_col = [col for col in df.columns if 'price' in col.lower() or 'average' in col.lower()]
if price_col:
    df[price_col[0]] = pd.to_numeric(df[price_col[0]], errors='coerce')

# Drop rows with missing year or price
df = df.dropna(subset=['Year', price_col[0]])

# Group by year and calculate average price
avg_price_per_year = df.groupby('Year')[price_col[0]].mean()

# Plot the results
plt.figure(figsize=(10, 6))
avg_price_per_year.plot(marker='o')
plt.title('Average Bread Price Per Year')
plt.xlabel('Year')
plt.ylabel('Average Price')
plt.grid(True)
plt.tight_layout()
plt.show()