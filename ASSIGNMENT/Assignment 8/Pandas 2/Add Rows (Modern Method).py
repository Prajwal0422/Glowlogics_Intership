import pandas as pd

d1 = pd.DataFrame([[7,8],[9,10]], columns=['x','y'])
d2 = pd.DataFrame([[11,12],[13,14]], columns=['x','y'])

d = pd.concat([d1,d2])
print(d)