from pylab import plotfile, show, gca
import matplotlib.cbook as cbook

fname = cbook.get_sample_data('/home/wuqili/datavis/amzn.csv', asfileobj=False)
plotfile(fname, (0,4,6 ), plotfuncs={'Volume':'bar'})
show()