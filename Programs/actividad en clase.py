"""MARSAGLIA EFFECT:
correlación entre los puntos aleatorios indica la falta de aleatoriedad"""

import numpy as np
from pylab import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from matplotlib import style

def IBMrandomNumbers(seed, N):
    x = np.zeros(N)
    num = np.zeros(N)

    x[0] = seed
    for i in range(0,N-1):
        x[i+1] = (65539*x[i])%(2**31)
        num[i+1] = x[i+1]/2**31

    num[0] = num[-1]
    return num

num = IBMrandomNumbers(91287, 10)


# Creamos la figura
fig = plt.figure()
# Agrrgamos un plano 3D
ax1 = fig.gca(projection='3d')
# Mostramos el gráfico
ax1.scatter3D(num[:-2], num[1:-1], num[2:], c='g', marker='o')
plt.show()


