import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['axes.facecolor']='#f8f8f8'
mpl.rcParams['grid.color'] = '#303030'
mpl.rcParams['lines.linestyle'] = '--'

x = [2400, 2350, 2400, 2290, 2100, 2380, 2300, 2280, 2210, 2390]
y = [4.4, 4.5, 4.2, 4.3, 4.0, 4.1, 3.9, 4.0, 4.3, 4.5]

a = '#6D0000'
r = '#00006F'
z = [a, a, a, r, r, a, r, r, a, a]

plt.figure(figsize=(11,11))
plt.scatter(x,y,c=z, s=600)

for i in range(1,5):
    X_plot = np.linspace(2490-i*2, 2150+i*2, 20)
    Y_plot = np.linspace(3.3+i*0.2, 5.0-i*0.2, 20)
    plt.plot(X_plot, Y_plot, c='gray')
    
plt.grid(True)
plt.xlabel('SAT Score', fontsize=18)
plt.ylabel('GPA', fontsize=18)
plt.title('Acceptance in College', fontsize=20)
plt.show()
plt.savefig('datavis/college acceptance')