import pandas as pd
import numpy as np
import sklearn.cross_validation as skc
import sklearn.neighbors as skn
# import sklearn.svm as sksS -- TESTED CHANGE

desired_width = 320
pd.set_option('display.width', desired_width)

ds = pd.read_csv('cancer.data',names=['id','clump_thickness','unif_cell_size','unif_cell_shape','marg_adhesion',
                                                'single_epith_cell_size','bare_nuclei','bland_chrome','norm_nucleoil',
                                      'mitoses','class'])


# print(ds['clump_thickness'].value_counts())
# print(ds.isnull().sum())
# print(ds.head())

# print(ds[ds.bare_nuclei == '?'])
# print(ds['bare_nuclei'][ds.bare_nuclei == '?'])
ds.replace('?',-9999, inplace=True)
# print(ds['bare_nuclei'][ds.bare_nuclei == '?'])
ds.drop('id',1,inplace=True)

X = np.array(ds.drop('class',1))
y = np.array(ds['class'])

print(len(X),len(y))

X_train, X_test, y_train, y_test = skc.train_test_split(X,y,test_size=0.2)

clf = skn.KNeighborsClassifier()
# clf.fit(X_train,y_train)
# pd.to_pickle(clf,'knn.clf')

clf = pd.read_pickle('knn.clf')
accuracy = clf.score(X_test,y_test)

print(accuracy)
