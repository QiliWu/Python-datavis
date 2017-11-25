import stochpy as stp
from pylab import rcParams
rcParams['figure.figsize'] = 12, 12
smod = stp.SSA()
smod.Model('dsmts-003-04.xml.psc')
smod.DoStochSim(end=35, mode='time', trajectories=2000)
smod.GetRegularGrid()
smod.PlotAverageSpeciesTimeSeries()