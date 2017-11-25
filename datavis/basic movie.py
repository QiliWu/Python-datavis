import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
fig = plt.figure()
ax = plt.axes(xlim=(0, 3.2), ylim=(-2.14, 2.14))
line, = ax.plot([], [], lw=2)
def init():
    line.set_data([], [])
    return line,


def animate(i):
    x = np.linspace(0, 2, 1000)
    xval = 2 * np.pi*(x-0.01*i)
    y = np.cos(xval)
    line.set_data(x,y)
    return line,
    
anim = animation.FuncAnimation(fig, animate, init_func=init, frames=200, interval=20, blit=True)
anim.save('basic_animation.mp4', fps=30)
plt.show()