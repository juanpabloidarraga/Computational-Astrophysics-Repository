"""MARSAGLIA EFFECT:
correlación entre los puntos aleatorios indica la falta de aleatoriedad"""

import numpy as np
from pylab import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from matplotlib import style

N = 1200
x=np.zeros(N)
num =np.zeros(N)
print(num)

x[0] = 9283983

for i in range(0,N-1):
    x[i+1] = (65539*x[i])%(2**31)
    num[i+1] = x[i+1]/2**31

num[0] = num[-1]





u=np.zeros(N)
u2=np.zeros(N)
u3=np.zeros(N)
print(u)
u[0:N] =num[0:N]
u2[0:N-1] =num[1:N] 
u3[0:N-2] =num[2:N]
u2[N-1] = u[0]
u3[N-2] = u[0]
u3[N-1] = u[1]


# Creamos la figura
fig = plt.figure()
# Agrrgamos un plano 3D
ax1 = fig.gca(projection='3d')
# Mostramos el gráfico
ax1.scatter3D(u, u2, u3, c='g', marker='o')
plt.show()


#x[0] = 4857964
u2[0] = x[0]/2**31

