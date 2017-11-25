from scipy.stats.kde import gaussian_kde
from scipy.stats import norm
from numpy import linspace, hstack
from pylab import plot, show, hist

sample1 = norm.rvs(loc=-1.0, scale=1, size=320)
sample2 = norm.rvs(loc=2.0, scale=0.6, size=320)
sample = hstack([sample1, sample2])

probDensityFun = gaussian_kde(sample)
plt.title('KDE Demonstration using Scipy and Numpy', fontsize=20)
x=linspace(-5,5, 200)
plot(x, probDensityFun(x),'r')
hist(sample, normed=1, alpha=0.45, color='purple')

plt.show()

plt.savefig('datavis/kde-scipy')