# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import pylab
from pylab import rcParams
import networkx as nx
import numpy as np

rcParams['figure.figsize'] = 10,10
G = nx.DiGraph()
G.add_edges_from([('K', 'I'), ('R', 'T'), ('V','T')], weight=3)
G.add_edges_from([('T', 'K'), ('I','T'), ('T','H')], weight=4)
G.add_edges_from([('I', 'R'), ('H', 'N')], weight=5)
G.add_edges_from([('R', 'N')], weight=6)

#these values to determine node colors
val_map = {'K':1.5, 'I':0.9, 'R':0.6, 'T':0.2}
values = [val_map.get(node, 1.0) for node in G.nodes()]
edge_labels = dict([((u,v,),d['weight']) for u,v,d in G.edges(data=True)])
#set edge colors
red_edges = [('R','T'), ('T','K')]
edge_colors = ['green' if not edge in red_edges else 'red' for edge in G.edges()]

#布局节点，方法有circular_layout：节点在一个圆环上均匀分布； random_layout：节点随机分布；shell_layout：节点在同心圆上分布
#spring_layout： 用Fruchterman-Reingold算法排列节点（这个算法我不了解，样子类似多中心放射状）
#spectral_layout：根据图的拉普拉斯特征向量排列节
pos = nx.circular_layout(G)
#nx.draw_networkx_edges(G, pos, width=2.0, alpha=0.65)
#nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
nx.draw(G, pos,node_color=values, node_size=1500, with_labels=True, edge_color=edge_colors, edge_cmap=plt.cm.Reds)
pylab.show()
plt.savefig('datavis/networkx-2')