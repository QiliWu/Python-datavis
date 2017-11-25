import networkx as nx
from pylab import rcParams

rcParams['figure.figsize'] = 12, 12
G = nx.read_gml('datavis/lesmiserables.gml')
G8 = G.copy()
dn = nx.degree(G8)

for n in G.nodes():
    if dn[n] <= 8:
        G8.remove_node(n)
        
pos = nx.spring_layout(G8)
nx.draw(G8, pos=pos, node_size=10, edge_color='b', alpha=0.45, font_size=9)
labels = nx.draw_networkx_labels(G8, pos=pos)

def valuegetter(*values):
    if len(values) == 1:
        item = values[0]
        def g(obj):
            #print 'obj--', obj
            return obj[item]
            
    else:
        def g(obj):
            return tuple(obj[item] for item in values)
    return g
    
def clustering_coefficient(G, vertex):
    neighbors = G[vertex].keys()
    if len(neighbors) == 1:
        return -1.0
    links = 0
    for node in neighbors:
        for u in neighbors:
            if u in G[node]:
                links += 1
    ccoeff = 2.0 * links/(len(neighbors)*(len(neighbors)-1))
    return links, len(neighbors), ccoeff
    
def calculate_centrality(G):
    degc = nx.degree_centrality(G)
    nx.set_node_attributes(G, degc,'degree_cent')
    degc_sorted = sorted(degc.items(),key=valuegetter(1), reverse=True)
    for key, value in degc_sorted[0:10]:
        print 'Degree Centrality:', key, value
    return G, degc
    
print 'Valjean', clustering_coefficient(G8, 'Valjean')
print 'Marius', clustering_coefficient(G8, 'Marius')  
print 'Gavroche', clustering_coefficient(G8, 'Gavroche') 
print 'Babet', clustering_coefficient(G8, 'Babet')
print 'Eponine', clustering_coefficient(G8, 'Eponine') 
print 'Courfeyrac', clustering_coefficient(G8, 'Courfeyrac')
print 'Comeferre', clustering_coefficient(G8, 'Combeferre')
calculate_centrality(G8)
