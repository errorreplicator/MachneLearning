import pandas as pd
import matplotlib.pyplot as mps
from mpl_toolkits.mplot3d import Axes3D


desired_width = 320
pd.set_option('display.width', desired_width)

mps.style.use('ggplot')
# ds = pd.read_csv('student.csv',sep=';')
# # print(ds.head())
# ds1 = ds['G1']
# ds2 = ds[['G3','G2','G1']]
# # ds1.plot.hist(alpha=0.5)
# # ds2.plot.hist(alpha=0.5)
# ds.plot.scatter(x='G3',y='G1')
# mps.show()

ds = pd.read_csv('wheat.data')

ds_ap = ds[['area','perimeter']]
ds_ga = ds[['groove','asymmetry']]


fig = mps.figure()
mps.suptitle('My first 3D')
ax = fig.add_subplot(111,projection='3d')

ax.set_xlabel("Area")
ax.set_ylabel("Perimeter")
ax.set_zlabel("Whead type")

ax.scatter(ds.area,ds.perimeter,ds.groove, c='r',marker='o')

# ds_ap.plot.hist(alpha=0.75)
# ds_ga.plot.hist(alpha=0.75)

mps.show()

# print(ds.head())
# print(ds.info())

