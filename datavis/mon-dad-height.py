# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
import seaborn as sns

students = pd.read_csv('datavis/ucdavis.csv')
g=sns.FacetGrid(students, hue='gender', palette='Set1', size=7)
g.map(plt.scatter, 'momheight', 'height', s=250, linewidth=0.5, edgecolor='#ffad40')
#这里不能设置color， 因为需要出现两种不同颜色的球
g.set_axis_labels('Mothers Height', 'Student Height')
g.add_legend()   #如果legend不在图外，则可以手动调整figure axis
plt.show()
plt.savefig('datavis/mom-height')

f = sns.FacetGrid(students, hue='gender', palette='Set2', size=7)

#本来尝试设置color=两种颜色，图像显示成功，但是最后legend还是只有一种颜色。
f.map(plt.scatter, 'dadheight', 'height',s=250, linewidth=0.5, edgecolor='white')

f.set_axis_labels('Fathers Height', 'Height')

f.add_legend()

plt.savefig('datavis/dad-height')

plt.show()