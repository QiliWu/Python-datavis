from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-4,4,0.25)
y = np.arange(-4,4,0.25)
X,Y = np.meshgrid(x,y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

fig = plt.figure(figsize(12,9))
ax = fig.gca(projection='3d')
surf = ax.plot_surface(X,Y,Z, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=False)
ax.set_zlim(-1.01,1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
fig.colorbar(surf, shrink=0.6, aspect=6)

plt.show()
plt.savefig('datavis/3d image')