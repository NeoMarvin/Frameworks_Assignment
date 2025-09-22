import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
try:
    df = pd.read_csv("project_assignment/region_date_metadata.csv")
    print("✔ Loaded region_date_metadata.csv successfully!")
except FileNotFoundError:
    print("❌ region_date_metadata.csv not found. Place it in the same folder as this script.")
    exit()

# Show dataset info
print(df.shape)
print(df.info())
print(df.head())

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

# Drop rows with missing Date
df = df.dropna(subset=["Date"])

# Basic statistics
print("\nStatistics on Recoveries:")
print(df["Recoveries"].describe())

# Group by Country and get average recoveries
avg_recoveries = df.groupby("Country_Region")["Recoveries"].mean().sort_values(ascending=False)
print("\nAverage Recoveries by Country:")
print(avg_recoveries.head())

# ---- VISUALIZATIONS ----

# 1. Line chart: recoveries over time (global sum)
daily_recoveries = df.groupby("Date")["Recoveries"].sum()
plt.figure(figsize=(10,5))
daily_recoveries.plot(kind="line")
plt.title("Total Recoveries Over Time")
plt.xlabel("Date")
plt.ylabel("Recoveries")
plt.show()

# 2. Bar chart: top 10 countries by average recoveries
plt.figure(figsize=(10,5))
avg_recoveries.head(10).plot(kind="bar")
plt.title("Top 10 Countries by Average Recoveries")
plt.xlabel("Country")
plt.ylabel("Avg Recoveries")
plt.show()

# 3. Histogram: distribution of recoveries
plt.figure(figsize=(8,5))
df["Recoveries"].plot(kind="hist", bins=30)
plt.title("Distribution of Recoveries")
plt.xlabel("Recoveries")
plt.show()

# 4. Scatter plot: Date vs Recoveries (just a sample)
plt.figure(figsize=(10,5))
plt.scatter(df["Date"], df["Recoveries"], alpha=0.3)
plt.title("Recoveries Over Time (Scatter)")
plt.xlabel("Date")
plt.ylabel("Recoveries")
plt.show()