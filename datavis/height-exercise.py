import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style='whitegrid')
students=pd.read_csv('datavis/ucdavis.csv')
x=students.height
y=students.exercise
z=students.exercise

cm = plt.cm.get_cmap('RdYlBu')
fig, ax = plt.subplots(figsize(12,10))

sc = ax.scatter(x,y,s=z*3, c=z, cmap=cm, linewidths=0.2, alpha=0.5)
ax.grid()
fig.colorbar(sc)

ax.set_xlabel('height')
ax.set_ylabel('exercise')

plt.show()
plt.savefig('datavis/height-exercise')