import math
import pandas as pd
import numpy as np

ds = pd.DataFrame(np.random.choice([0,4,'ta',np.nan], size=(10,5)),columns=['stq','2nd','3rd','4th','5th'])


##print(ds.loc[:,['stq','5th']][ds.stq.str.contains('^t')]) # list down two columns where string begins with 't'
# print(ds)

# print(ds.loc[:,'4th':'5th'][ds['4th'] == 4])
# print(ds[pd.isnull(ds).any(axis=1)])
print(ds[ds['stq'].str.contains('\?')])
