import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('dataset .csv')

# Line Chart - COVID Cases Over Time
plt.figure(figsize=(10,5))
plt.plot(df[df["location"] == "United States"]["date"], df[df["location"] == "United States"]["total_cases"], label="USA Cases", color="blue")
plt.xlabel("Date")
plt.ylabel("Total Cases")
plt.title("COVID-19 Cases Over Time in USA")
plt.legend()
plt.show()

# Bar Chart - Top 10 Countries by Total Cases
top_countries = df.groupby("location")["total_cases"].max().sort_values(ascending=False).head(10)
plt.figure(figsize=(10,5))
sns.barplot(x=top_countries.index, y=top_countries.values, palette="coolwarm")
plt.xticks(rotation=45)
plt.xlabel("Country")
plt.ylabel("Total Cases")
plt.title("Top 10 Countries by Total Cases")
plt.show()

# Histogram - Distribution of Total Cases
plt.figure(figsize=(10,5))
plt.hist(df["total_cases"].dropna(), bins=50, color="blue", edgecolor="black")
plt.xlabel("Total Cases")
plt.ylabel("Frequency")
plt.title("Distribution of COVID-19 Cases")
plt.show()

# Scatter Plot - Cases vs Deaths
plt.figure(figsize=(10,5))
sns.scatterplot(x=df["total_cases"], y=df["total_deaths"], hue=df["location"], alpha=0.5)
plt.xlabel("Total Cases")
plt.ylabel("Total Deaths")
plt.title("COVID-19 Cases vs Deaths")
plt.show()
