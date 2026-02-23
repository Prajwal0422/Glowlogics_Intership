import pandas as pd

info = pd.DataFrame({
    'col1':[7,1,8,3],
    'col2':[8,12,4,9]
})

sorted_df = info.sort_values(by='col2')
print(sorted_df)