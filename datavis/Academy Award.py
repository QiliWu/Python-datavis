# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

winnersplot = (142.6, 125.3, 62, 81,145.6, 319.4, 178.1)
nomineesplot=(109.4, 94.8, 60.7, 44.6, 116.9, 262.5, 102)
N=7
ind=np.arange(N)
width=0.35

fig, ax = plt.subplots()
winners = ax.bar(ind,winnersplot, width, color='#ffad00')
nominees = ax.bar(ind+width, nomineesplot, width, color='#9b3c38')
ax.set_xticks(ind+width)
ax.set_xticklabels(('Best Picture', 'Director', 'Best Actor', 'Best Actress', 'Editing', 'Visual Effects', 'Cinematography'))
ax.legend((winners[0], nominees[0]), ('Academy Award Winners', 'Academy Award Nominees'))

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        hcap = '$'+str(height)+'M'
        ax.text(rect.get_x()+width/2, height, hcap, ha='center', va='bottom', rotation='vertical')
        

autolabel(winners)
autolabel(nominees)

plt.show()
#调整y轴大小
ax.set_ylim([0,400])
#调整X轴上label字体大小
for label in ax.get_xticklabels():
    label.set_fontsize(9)
#旋转xticklabels
plt.setp(ax.xaxis.get_majorticklabels(), rotation=-45)    
#调整底边空白间距
plt.subplots_adjust(bottom=0.15)
#调整legend的位置至左上方, 取代了之前的那个
ax.legend((winners[0], nominees[0]), ('Academy Award Winners', 'Academy Award Nominees'),loc='upper left')    

plt.show()
plt.savefig('Academy Award') #保存至当前目录，png格式。