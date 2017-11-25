import matplotlib.pyplot as plt
import numpy as np

'''
Geometric Brownian Motion with drift!
u=drift factor
sigma: Volatility
T: time span
dt: length of steps
S0: Stock Price in t=0
W: Brownian Motion with Drift N[0,1]
'''
fig = plt.figure(figsize=(10, 10))

T = 2
mu = 0.1
sigma = 0.04
S0 = 20
dt = 0.01
N = round(T/dt)
t = np.linspace(0, T, N)

W = np.random.standard_normal(size=N)
W = np.cumsum(W)*np.sqrt(dt)

X = (mu-0.5*sigma**2)*t + sigma*W
S = S0*np.exp(X)

plt.plot(t, S, lw=2)
plt.xlabel('Time t', fontsize=16)
plt.ylabel('S', fontsize=16)
plt.title('Geometric Brownian Motion (Simulation)', fontsize=20)