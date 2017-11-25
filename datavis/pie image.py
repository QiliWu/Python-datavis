# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

labels = ['Computer Science', 'Foregin Language', 'Analytical Chemistry', 'Education', 'Humanities', 'Physics', 'Biology', 'Math and Statistics','Engineering']
sizes = [21, 4, 7, 7, 8, 9, 10, 15, 19]

colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral', 'red', 'purple', '#f280de', 'orange', 'green']
explode=(0,0,0,0,0,0,0,0,0.1)

plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%')
plt.axis('equal')  #调整图片x， y轴比例，使其相等，得到正圆
plt.show()
plt.savefig('datavis/pie image')