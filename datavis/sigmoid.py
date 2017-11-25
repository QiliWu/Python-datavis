import matplotlib.pyplot as plt
import matplotlib
import random
import math
import numpy as np
import scipy, scipy.stats
import pandas as pd

x = np.linspace(-10, 10, 100)
y1 = 1.0 / (1.0+np.exp(-x))
y2 = 1.0 / (1.0+np.exp(-x/2))
y3 = 1.0 / (1.0+np.exp(-x/10))

plt.figure()
plt.title('Sigmoid Functions vs LineSpace')
plt.plot(x, y1, 'r-', lw=2)
plt.plot(x, y3, 'b-', lw=2)
plt.legend(['y1', 'y2', 'y3'])
plt.xlabel('x')
plt.ylabel('y')
plt.show()
plt.savefig('datavis/sigmoid-1')