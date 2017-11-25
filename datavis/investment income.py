import numpy as np
import matplotlib.pyplot as plt
years = np.arange(2010, 2025)
y1 = 10000*(1.06**(years-2010))
y2=10000+833.33*(years-2010)

plt.grid()
plt.plot(years, y2, linewidth=4, color='b')
plt.plot(years, y1, linewidth=4, color='r')
plt.xlim(2010, 2024)
plt.ylim(10000, 24000)
plt.xlabel('Year', fontsize=16)
plt.ylabel('Sum_Money', fontsize=16)
plt.legend(['y2=10000+833.33*(years-2010)','y1 = 10000*(1.06**(years-2010))'], loc='upper left')

plt.show()
plt.savefig('datavis/investment income')
