import numpy as np

import matplotlib.pyplot as plt

x = np.linspace(0, 8*np.pi, 100)
y = np.sin(x)
y = np.sin(x/2)

yinterp = np.interp(x,x,y)

plt.plot(x,y,'o')

plt.plot(x, yinterp, '-x')

plt.savefig('datavis/sin-interp')