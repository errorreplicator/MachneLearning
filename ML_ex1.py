# import Quandl
import pandas as pd
import math
import numpy as np
import sklearn as sk
import sklearn.preprocessing as skp, sklearn.svm, sklearn.cross_validation, sklearn.linear_model
import pickle

desired_width = 320
pd.set_option('display.width', desired_width)

# ds = Quandl.get("WIKI/GOOGL", authtoken="_VC8mdqyTzENHcUoUxnu")
# pd.to_pickle(ds,'GoogleStock.pickle')

ds = pd.read_pickle('GoogleStock.pickle')
# print(ds.head())

ds = ds[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume']]

ds['HL_PCT'] = (ds['Adj. High'] - ds['Adj. Low']) / ds['Adj. Close'] * 100.0
ds['PCT_change'] = (ds['Adj. Close'] - ds['Adj. Open']) / ds['Adj. Open'] * 100.0

ds = ds[['Adj. Close', 'HL_PCT', 'PCT_change', 'Adj. Volume']]
# print(ds.head())
ds = pd.DataFrame(ds)


forecast_col = 'Adj. Close'
forecast_out = math.ceil(0.001 * len(ds))

ds['Label'] = ds[forecast_col].shift(-forecast_out)

ds.fillna(-9999, inplace=True)
# print(ds.isnull().sum())
# print(ds.isnull().sum())
# print(ds.tail())
X = np.array(ds.drop(['Label'],1))
y = np.array(ds['Label'])


X = skp.scale(X)
y = np.array(ds['Label'])
X_train, X_test, y_train, y_test = sklearn.cross_validation.train_test_split(X,y,test_size=0.2)

clf = sklearn.linear_model.LinearRegression()
# clf = sklearn.svm.SVR(kernel='poly')
# print(len(X),len(y))
clf.fit(X_train,y_train)
pd.to_pickle(clf,'LinReg.clf')

clf = pd.read_pickle('LinReg.clf')

accurasy = clf.score(X_test,y_test)
print(accurasy)

