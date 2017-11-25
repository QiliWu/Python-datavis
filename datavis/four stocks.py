# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt

amzn = pd.read_csv('datavis/AMZN.csv')
fb = pd.read_csv('datavis/FB.csv')
aapl = pd.read_csv('datavis/AAPL.csv')
goog = pd.read_csv('datavis/GOOG.csv')

data = amzn
data['amzn'] = amzn['Adj Close']
data['fb'] = fb['Adj Close']
data['aapl'] = aapl['Adj Close']
data['goog'] = goog['Adj Close']

del data['Open']
del data['High']
del data['Low']
del data['Close']
del data['Adj Close']
del data['Volume']

data = data.set_index(keys='Date')data = data.set_index(keys='Date')
retn = data.apply(pd.np.log).diff()
retn = data.apply(pd.np.log)

pd.tools.plotting.scatter_matrix(retn, figsize=(10, 10))  # default: diagonal=hist
pd.tools.plotting.scatter_matrix(retn, figsize(10,10), diagonal='kde')

retn.corr()
retn.skew()#偏度： 左正右负
retn.kurt()#峰度： 越尖锐， 值越大