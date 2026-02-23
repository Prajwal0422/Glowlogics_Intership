import pandas as pd
import numpy as np
a=pd.Series(['java','c','c++',np.nan])
print(a.map({'java':'Core'}))

x=['python','pandas']
df = pd.DataFrame(x)
print(df)

info = {'one':pd.Series([1,2,3,4,5,6],index=['a','b','c','d','e'])}

d1=pd.DataFrame(info)
print (d1['one'])
