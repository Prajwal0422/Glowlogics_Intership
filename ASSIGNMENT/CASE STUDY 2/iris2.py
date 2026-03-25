import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# LOAD DATA
df = pd.read_csv("state_level_latest.csv")

print("First Rows")
print(df.head())

print("\nInfo")
print(df.info())

print("\nSummary")
print(df.describe())

# GROUPING (Example – change column names if needed)
# Suppose dataset has 'State' and 'Value' columns

state_group = df.groupby("State").sum()

print("\nGrouped Data")
print(state_group)

# BAR CHART
state_group.plot(kind="bar", figsize=(12,6))
plt.title("State Level Comparison")
plt.ylabel("Total Value")
plt.show()

# TOP 10 STATES
top10 = state_group.sort_values(by=state_group.columns[0], ascending=False).head(10)

top10.plot(kind="bar", color="green")
plt.title("Top 10 States")
plt.show()

# HEATMAP (Correlation)
sns.heatmap(df.corr(), annot=True)
plt.title("Correlation Heatmap")
plt.show()