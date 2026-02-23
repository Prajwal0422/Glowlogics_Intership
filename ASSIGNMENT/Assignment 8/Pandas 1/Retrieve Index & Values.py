import pandas as pd

x = pd.Series([2,4,6,8])
y = pd.Series([11.2,18.6,22.5], index=['a','b','c'])

print(x.index)
print(x.values)

print(y.index)
print(y.values)