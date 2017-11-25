# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from scipy import interpolate

t = np.arange(0, 2.5, 0.1)
x = np.sin(2*np.pi*t)
y = np.cos(2*np.pi*t)

tck, uarray = sp.interpolate.splprep([x,y], s=0)
unew = np.arange(0, 1.01, 0.01)
values = sp.interpolate.splev(unew, tck)

plt.figure(figsize=(10,10))
plt.plot(x, y , 'x', values[0], values[1], np.sin(2*np.pi*unew), np.cos(2*np.pi*unew), x, y,'b')
plt.legend(['Linear', 'Cubic Spline', 'True'])
plt.axis([-1.25,1.25, -1.25, 1.25])
plt.title('Parametric Spline Interpolation Curve', fontsize=18)
plt.show()
plt.savefig('datavis/Spline Interpolation')

#将上图拆开来分解为四个图
fig = plt.figure()
ax1 = fig.add_subplot(221)
ax1.plot(x,y, 'x')
ax2 = fig.add_subplot(222)
ax2.plot(values[0], values[1])
ax3 = fig.add_subplot(223)
ax3.plot(np.sin(2*np.pi*unew), np.cos(2*np.pi*unew), 'g')
ax4 = fig.add_subplot(224)
ax4.plot(x, y ,'b')
fig.suptitle('Split Figures in Spline Interpolation', fontsize=18)
plt.show()
plt.savefig('datavis/Split Spline')