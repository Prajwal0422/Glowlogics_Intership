import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# LOAD DATA
df = pd.read_excel("india_lpg_crisis_dataset_2026.xlsx")

print("First Rows")
print(df.head())

print("\nInfo")
print(df.info())

print("\nSummary")
print(df.describe())


# HANDLE MISSING VALUES
df = df.dropna()

# TREND ANALYSIS (Example – change column names if needed)
# Suppose dataset has 'Year' and 'Demand'

year_group = df.groupby("Year").sum()

print("\nYearly Trend")
print(year_group)

year_group.plot(kind="line", figsize=(10,5))
plt.title("LPG Demand Trend Over Years")
plt.ylabel("Demand")
plt.show()


# STATE WISE ANALYSIS
state_group = df.groupby("State").sum()

state_group.sort_values(by=state_group.columns[0], ascending=False).head(10).plot(
    kind="bar", color="orange"
)

plt.title("Top 10 States LPG Demand")
plt.show()


# CORRELATION
sns.heatmap(df.corr(), annot=True)
plt.title("Correlation Heatmap")
plt.show()