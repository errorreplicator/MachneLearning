import pandas as pd
import numpy as np
import re

pd.set_option('display.width', 320)

ds = pd.read_csv('kidney_disease.csv')

# print(ds.info())
ds.dropna(inplace=True)
ds = ds[['bgr','rc','wc']]
ds.reset_index(inplace=True)
ds = ds[['bgr','rc','wc']]


##print(ds[~ds.wc.apply(lambda x: x.isnumeric())])

##print(ds[ds.wc.str.contains('\t')])


## print(ds[ds.rc.str.startswith('2', na=False)]) #checks if string begun with curtain digit
##print(ds[ds.rc.str.isdigit()]) # checks if the string is digits - does not work with floats since there is a dot 3.4

# print(ds.applymap(np.isreal))

## print(ds[ds['rc'].apply(lambda x: type(x) not in [int, np.int64, float, np.float64])])

# print(ds[~ds.applymap(np.isreal).all(1)])
#print(ds['wc'][ds['wc']=='\t'])
# ds['wc'] = ds['wc'].astype(str).convert_objects(convert_numeric=True)

##ds.wc = pd.to_numeric(ds.wc)
##ds.rc = pd.to_numeric(ds.rc)

##ds['rc'] = ds['rc'].astype(np.float64)
##ds['wc'] = ds['wc'].astype(np.int64)
# ds = ds[~ds.applymap(np.isreal).all(1)]


# print(ds.shape)
# print(ds.info())

# print(ds)