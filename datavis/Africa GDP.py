import squarify
import matplotlib.pyplot as plt
import matplotlib.cm
import numpy as np

x = 0.
y = 0.
width = 950
height = 733

fig = plt.figure(figsize=(15, 12))
ax = fig.add_subplot(111, axisbg='white')

values = [285.4, 188.4, 173, 140.6, 91.4, 75.5, 62.3, 39.6, 29.4, 28.5, 26.2, 22.2]
labels = ['South Africa', 'Egypt', 'Nigeria', 'Algeria', 'Morocco', 'Angola', 'Libya', 'Tunisia', 'Kenya', 'Ethiopia', 'Ghana', 'Cameron']
colors = [0]*11
for i in range(11):
    colors[i] = tuple(np.random.randint(0,255,3)/255.0)
    

initvalues = values
values = squarify.normalize_sizes(values, width, height)
rects = squarify.padded_squarify(values, x, y, width, height)

cmap = matplotlib.cm.get_cmap()
color = [cmap(random.random()) for i in range(len(values))]
x = [rect['x'] for rect in rects]
y = [rect['y'] for rect in rects]
dx = [rect['dx'] for rect in rects]
dy = [rect['dy'] for rect in rects]
ax.bar(x, dy, width=dx, bottom=y, color=colors, label=labels, align='edge')

va = 'center'
idx=1
for l,r,v in zip(labels, rects, initvalues):
    x,y,dx,dy = r['x'], r['y'], r['dx'], r['dy']
    ax.text(x+dx/2, y+dy/2+10, str(idx)+'--> '+l, va=va, ha='center', color='white', fontsize=14)
    ax.text(x+dx/2, y+dy/2-12, '($'+str(v)+'b)', va=va, ha='center', color='white', fontsize=12)
    idx=idx+1
    
ax.set_xlim(0, 1000)
ax.set_ylim(0, 1000)   
plt.title('Top 12 GDP Africa Country', fontsize=20)
plt.savefig('datavis/Africa-GDP')