import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

amzn = pd.read_csv('datavis/AMZN.csv')
amzn['Volatility'] = np.log(amzn['Close']/amzn['Close'].shift(1))
amzn=amzn.set_index(keys='Date')
amzn[['Close', 'Volatility']].plot(figsize=(12, 10), subplots=True, color='red')
plt.xlabel('Date', fontsize=18)
f=plt.gcf()
f.suptitle('Volatility of AMZN Stock',fontsize=20)
plt.show()
plt.savefig('datavis/Volatility of AMZN Stock')