import networkx as nx
from pylab import rcParams

rcParams['figure.figsize'] = 12, 12
G = nx.read_gml('datavis/lesmiserables.gml')
G8 = G.copy()
dn = nx.degree(G8)

for n in G8.nodes():
    if dn[n] <= 8:
        G.remove_node(n)
        
pos = nx.spring_layout(G)
nx.draw(G, pos=pos, node_size=10, edge_color='b', alpha=0.45, font_size=9)
labels = nx.draw_networkx_labels(G, pos=pos)