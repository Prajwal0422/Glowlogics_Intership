import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("pokemon.csv")

print(df.head())
print(df.describe())

# Choose 4 parameters
params = ["HP","Attack","Defense","Speed"]

for col in params:
    plt.figure(figsize=(6,4))
    sns.scatterplot(x=df[col], y=df["Total"])
    plt.title(f"{col} vs Total")
    plt.show()

# Correlation Heatmap
plt.figure(figsize=(10,6))
sns.heatmap(df.corr(),annot=True)
plt.title("Pokemon Correlation")
plt.show()