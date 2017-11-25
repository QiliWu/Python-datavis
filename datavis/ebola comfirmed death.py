import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
from datetime import datetime

eboladata=pd.read_csv('datavis/ebola.csv')
filtered = eboladata[eboladata['value']>0]
filtereddata = filtered[filtered['Indicator'].str.contains('death')]

Guineadata = filtereddata[filtereddata['Country']=='Guinea']
Guineadata = Guineadata[Guineadata['Indicator']=='Cumulative number of confirmed Ebola deaths']
Sierradata = filtereddata[filtereddata['Country']=='Sierra Leone']
Sierradata = Sierradata[Sierradata['Indicator']=='Cumulative number of confirmed Ebola deaths']
Liberiadata = filtereddata[filtereddata['Country'].str.contains('Liberia')]   #some named as Liberia 2
Liberiadata = Liberiadata[Liberiadata['Indicator']=='Cumulative number of confirmed Ebola deaths']

Guineadata = Guineadata.sort(columns='Date')
Sierradata = Sierradata.sort_values(by='Date')
Liberiadata = Liberiadata.sort_values(by='Date')

g_x=[datetime.strptime(date, '%Y-%m-%d').date() for date in Guineadata['Date']]
g_y = Guineadata['value']
s_x=[datetime.strptime(date, '%Y-%m-%d').date() for date in Sierradata['Date']]
s_y = Sierradata['value']
l_x=[datetime.strptime(date, '%Y-%m-%d').date() for date in Liberiadata['Date']]
l_y = Liberiadata['value']

plt.figure(figsize=(10,10))
plt.plot(g_x, g_y, color='red', linewidth=2, label='Guinea')
plt.plot(s_x, s_y, color='orange', linewidth=2, label='Sierra Leone')
plt.plot(l_x, l_y, color='blue', linewidth=2, label='Liberia')
plt.xlabel('Date', fontsize=18)
plt.ylabel('Number of Ebola Deaths', fontsize=18)
plt.legend()