import numpy as np
import matplotlib.pyplot as plt

S0 = 100
r = 0.05
sigma = 0.25
T = 2.0

x0 = 0
k = 1.8
theta = 0.24
i = 100000
M = 50
dt = T/M

def srd_euler():
    xh = np.zeros((M+1, i))
    xl = np.zeros_like(xh)
    xh[0] = x0
    xl[0] = x0
    for t in range(1, M+1):
        xh[t] = (xh[t-1] + k*(theta-np.maximum(xh[t-1], 0))*dt+theta*np.sqrt(np.maximum(xh[t-1], 0)*dt)*np.random.standard_normal(i))
    print xh[:5, :10]
    xl = np.maximum(xh, 0)
    print xl[:5, :10]
    print xl == xh
    return xl

xl = srd_euler()
#plt.figure(figsize=(10, 6))
plt.figure()
plt.subplot(211)
plt.hist(xl[-1], bins=30, color='#98DE2f', alpha=0.85)
plt.xlabel('Value', fontsize=16)
plt.ylabel('Frequency', fontsize=16)
plt.grid(False)

plt.subplot(212)
plt.plot(xl[:,:10], lw=2.2)
plt.xlabel('Time', fontsize=16)
plt.ylabel('Index Level', fontsize=16)
plt.suptitle('Square-Root Diffusion - Simulation', fontsize=20)
plt.subplots_adjust(left=0.15, hspace=0.4)
plt.show()    