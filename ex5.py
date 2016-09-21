import pandas as pd
import numpy as np

desired_width = 320
pd.set_option('display.width', desired_width)

# ds = pd.read_html('https://github.com/authman/DAT210x/blob/master/Module2/Datasets/tutorial.csv')
# ds = pd.DataFrame(ds[0])
# ds.drop('col0',1,inplace=True)
# ds.rename(columns={'col1':'First','col2':'2nd','col3':'3rd','Unnamed: 4':'4th'}, inplace=True)
# ds.to_csv('tutorial.csv')
# ds = pd.read_csv('tutorial.csv')
# ds.drop('Unnamed: 0',1,inplace=True)
# # print(ds.loc[1:4,'2nd':])
# print(ds.describe())

ds = pd.read_csv('census.dat',names=['education', 'age', 'capital-gain', 'race', 'capital-loss', 'hours-per-week', 'sex', 'classification'])

# print(ds.isnull().sum())
# print(ds.sum())
# print(ds.head())
# print(ds['capital-gain'][ds['capital-gain'] == '?'])
# print(ds['capital-gain'] == '?')

ds.replace('?',-9999,inplace=True)

ds['capital-gain'] = ds['capital-gain'].astype(np.int64)

# print(ds['capital-gain'].sum())
print(ds.info())
# print(ds.head())




