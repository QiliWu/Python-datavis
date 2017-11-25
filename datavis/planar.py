import planarity
import networkx as nx
G8 = nx.complete_graph(8)
G8.nodes
G8.edges
planarity.is_planar(G8)
K = planarity.kuratowski_subgraph(G8)
K.edges
K.nodes
nx.draw(G8)