import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("datasets/iris.csv")

print(df.head())
print(df.describe())

df["sepal_length"].hist()
plt.show()