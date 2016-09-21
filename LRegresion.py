import matplotlib.pyplot as mlp

x = [1,2,3,4,5,6]
y = [5,4,6,5,6,7]

mlp.scatter(x,y)
mlp.ylim(0,10)
mlp.xlim(0,10)
mlp.show()