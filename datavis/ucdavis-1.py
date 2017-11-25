import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
import seaborn as sns

fig, axes = plt.subplots(nrows=2, ncols=2)

students = pd.read_csv('datavis/ucdavis.csv')

first = students.pivot_table('sleep', index='gpa', columns='gender')
second = students.pivot_table('exercise', index='sleep', columns='gender')
third = students.pivot_table('gpa', index='tv', columns='gender')
four = students.pivot_table('gpa', index='exercise', columns='gender')

axes[0,0].scatter(first.index, first['Female'])
axes[0,0].scatter(first.index, first['Male'])
axes[0,0].set_xlabel('gpa')
axes[0,0].set_ylabel('sleep')
