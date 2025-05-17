# Task 1: Load and Explore the Dataset
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset (Error Handling)
try:
    df = pd.read_csv("dataset.csv")
except FileNotFoundError:
    print("Error: dataset.csv not found!")

# Display first few rows
print(df.head())

# Check structure & missing values
print(df.info())
print(df.isnull().sum())

# Clean data (drop missing values)
df.dropna(inplace=True)

# Task 2: Basic Data Analysis
# Line Chart (Trend over time)
plt.figure(figsize=(8,5))
df.plot(x="date_column", y="numeric_column", kind="line", marker='o')
plt.title("Trends Over Time")
plt.xlabel("Date")
plt.ylabel("Value")
plt.show()

# Bar Chart (Comparison across categories)
plt.figure(figsize=(8,5))
sns.barplot(x="category_column", y="numeric_column", data=df, palette="coolwarm")
plt.title("Category-wise Comparison")
plt.xlabel("Category")
plt.ylabel("Average Value")
plt.show()

# Histogram (Distribution of numeric data)
plt.figure(figsize=(8,5))
plt.hist(df["numeric_column"], bins=20, color="blue", edgecolor="black")
plt.title("Histogram of Numeric Column")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

# Scatter Plot (Relationship between two variables)
plt.figure(figsize=(8,5))
sns.scatterplot(x="numeric_x", y="numeric_y", data=df, hue="category_column")
plt.title("Scatter Plot of Two Variables")
plt.xlabel("X Variable")
plt.ylabel("Y Variable")
plt.show()


