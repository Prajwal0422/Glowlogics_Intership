import pandas as pd
import numpy as np

a = pd.Series(['Java','C','C++', np.nan])

print(a.map({'Java':'Core'}))

print(a.map('I like {}'.format, na_action='ignore'))