import math
import pandas as pd
import numpy as np

ds = pd.DataFrame(np.random.choice([0,1,2,3,4,'?',np.nan], size=(10,5)),columns=['1st','2nd','3rd','4th','5th'])


# print(ds.loc[:,'4th':'5th'][ds['4th'] == 4])
print(ds)
# print(ds[pd.isnull(ds).any(axis=1)])
# print(ds[ds['1st'].str.contains('?')])
