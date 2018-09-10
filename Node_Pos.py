#https://stackoverflow.com/questions/11804730/networkx-add-node-with-specific-position

import networkx as nx
import matplotlib.pyplot as plt

# to draw a SFG nodes MUST be in the same line >> y is const
# a problem developed here .. just one edge appears and the others are below
# sol : draw curved edges using matplotlip
# note : self-loop
pos = {0: (40, 20), 1: (30, 20), 2: (20, 20), 3: (10, 20)}
X=nx.MultiDiGraph()
nx.draw_networkx_nodes(X,pos,node_size=3000,nodelist=[0,1,2,3],node_color='r')

X.add_nodes_from(pos.keys())

X.add_edges_from([(1,2),(1,3),(2 , 0),(3 , 2) , (2,2)])


# If you want the position of the node as a node attribute, you could do that as well:
'''

for n, p in pos.iteritems():
    X.node[n]['pos'] = p

'''

nx.draw(X, pos)
plt.show()
