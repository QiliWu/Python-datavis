import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
from datetime import datetime

eboladata=pd.read_csv('datavis/ebola.csv')
filtered = eboladata[eboladata['value']>0]
f_data = filtered[filtered['Indicator'] =='Cumulative number of confirmed, probable and suspected Ebola deaths']
f_data['Date'] = [datetime.strptime(date, '%Y-%m-%d') for date in f_data['Date']]

g_data = f_data[f_data['Country']=='Guinea']
s_data = f_data[f_data['Country']=='Sierra Leone']
l_data = f_data[f_data['Country']=='Liberia']
g_x = g_data['Date']
s_x = s_data['Date']
l_x = l_data['Date']
g_y = g_data['value']
s_y = s_data['value']
l_y = l_data['value']

plt.figure(figsize=(10,10))
plt.plot(g_x, g_y, color='red', linewidth=4, label='Guinea')
plt.plot(s_x, s_y, color='blue', linewidth=4, label='Sierra Leone')
plt.plot(l_x, l_y, color='green', linewidth=4, label='Liberia')
plt.legend()
plt.xlabel('Date', fontsize=18)
plt.ylabel('Number of Ebola Deaths', fontsize=18)
plt.title('Probable and Suspected Ebola Deaths', fontsize=20)
plt.show()
plt.savefig('datavis/Ebola-3')