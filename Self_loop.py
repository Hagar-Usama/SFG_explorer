# https://stackoverflow.com/questions/49340520/matplotlib-and-networkx-drawing-a-self-loop-node

import networkx as nx
from networkx.drawing.nx_agraph import to_agraph
import matplotlib.pyplot as plt
# define the graph as per your question
G=nx.MultiDiGraph([(1,2),(1,1),(1,2),(2,3),(3,4),(2,4),
    (1,2),(1,2),(1,2),(2,3),(3,4),(2,4)])

# add graphviz layout options (see https://stackoverflow.com/a/39662097)
G.graph['edge'] = {'arrowsize': '0.6', 'splines': 'curved'}
G.graph['graph'] = {'scale': '3'}

# adding attributes to edges in multigraphs is more complicated but see
# https://stackoverflow.com/a/26694158
G[1][1][0]['color']='red'

A = to_agraph(G)
A.layout('dot')

plt.show()
# A.draw('multi.png')
