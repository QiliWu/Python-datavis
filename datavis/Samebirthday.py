import numpy as np
import matplotlib.pyplot as plt
from math import log

trytimes=10000

times = 0

for i in range(trytimes):
    sameday=0
    y = [0]*365
    for j in range(30):
        day = np.random.randint(0,365)
        y[day] += 1
        if y[day] > 1:
            sameday += 1
    if sameday>0:
        times += 1
print times    
prop = times*1.0/trytimes
print prop

prop2 = 1-(np.arange(336, 366)/365).prod()