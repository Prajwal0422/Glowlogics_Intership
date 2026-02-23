import pandas as pd

info = {
    'one': pd.Series([1,2,3,4,5,6], index=['a','b','c','d','e','f']),
    'two': pd.Series([1,2,3,4,5,6,7,8], index=['a','b','c','d','e','f','g','h'])
}

df = pd.DataFrame(info)
print(df['one'])