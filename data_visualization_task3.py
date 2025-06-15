
# Task 3: Data Visualization - CodeAlpha Internship
# Author: Anurag Bhagat

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load the dataset
df = pd.read_csv('data/sample_data.csv')  # Make sure this file exists in the data/ folder

# Basic data overview
print("First 5 rows of the dataset:")
print(df.head())
print("\nDataset Information:")
print(df.info())
print("\nSummary Statistics:")
print(df.describe())

# Handling missing values (example)
df = df.dropna()

# Histogram - Distribution of a numerical column (replace 'sales' with your column)
plt.figure(figsize=(8, 5))
sns.histplot(df['sales'], bins=30, kde=True)
plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("visuals/sales_distribution.png")
plt.show()

# Correlation heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("visuals/correlation_heatmap.png")
plt.show()

# Line plot - Trend over time (replace 'date' and 'sales' with actual columns)
fig = px.line(df, x='date', y='sales', title='Sales Over Time')
fig.write_html("visuals/sales_trend.html")
fig.show()
