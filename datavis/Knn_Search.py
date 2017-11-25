from numpy import random, argsort, sqrt
from pylab import plot, show
import matplotlib.pyplot as plt

def knn_search(x, data, K):
    """k nearest neighbors"""
    ndata = data.shape[1]
    K = K if K < ndata else ndata
    sqd = sqrt(((data - x[:,:ndata])**2).sum(axis=0))
    idx = argsort(sqd)
    return idx[:K]
    
data = random.rand(2, 200)
x = random.rand(2,1)
neig_idx = knn_search(x, data, 10)
plt.figure(figsize=(12, 12))

plot(data[0,:], data[1,:],'o', x[0,0], x[1,0], 'o', color='#9a88a1', markersize=20)
#highlighting the neighbors
plot(data[0,neig_idx], data[1, neig_idx], 'o', markerfacecolor='#BBE4B4',markersize=22, markeredgewidth=1)
show()