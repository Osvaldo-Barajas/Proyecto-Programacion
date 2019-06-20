import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import csv
from numpy.random import rand
X=Y=Z=[]

arch='coordenadas.csv'
with open(arch) as csvfile:
    reader=csv.DictReader(csvfile)
    for row in reader:
        X=float(row['Latitud'])
        Y=float(row['Longitud'])

X,Y=np.meshgrid(X,Y)
fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
ax.scatter(X,Y, c='r',marker='o')
ax.scatter(Y,X, c='r',marker='x')
plt.show()
