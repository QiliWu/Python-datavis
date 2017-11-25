import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_palette('hls')
matplotlib.rc('figure', figsize=(10,6))
data=np.random.randn(250)
sns.distplot(data, color='#ff8000')
plt.title('KDE Demonstration using Seaborn and Matplotlib')

plt.show()
plt.savefig('datavis/KDE.csv')