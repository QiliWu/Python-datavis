import numpy as np
from math import log
import matplotlib.pyplot as plt

x=[]
y=[]

def generateProfit(d):
    global s
    if d>=s:
        return 0.6*s
    else:
        return (1.0*d - 0.4*s)
        
#maxprofit = 0

for s in range(20, 300):
    x.append(s)
    maxprofit = 0
    for i in range(1000):
        d=np.random.randint(80, 140)
        profit = generateProfit(d)
        if profit > maxprofit:
            maxprofit=profit
    y.append(maxprofit)
plt.plot(x, y)
plt.show()
print x[y.index(max(y))] 
print y
            