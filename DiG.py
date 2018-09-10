#https://stackoverflow.com/questions/47094949/labeling-edges-in-networkx

import networkx as nx
import matplotlib.pyplot as plt

# Edges of my graph ( node to node )
edges=[['A','B'],['B','C'],['B','D'] , ['D' , 'E'] , ['E', 'A']]

# Creating a graph G
G=nx.Graph()

# Adding Edges
G.add_edges_from(edges)

#
pos = nx.spring_layout(G)

# Opening a figure
plt.figure()

# details of drawing
nx.draw(G,pos,edge_color='black',width=1,linewidths=1,\
node_size=500,node_color='pink',alpha=0.9,\
labels={node:node for node in G.nodes()})


nx.draw_networkx_edge_labels(G,pos,edge_labels={('A','B'):'G1',\
('B','C'):'G2',('B','D'):'G3'},font_color='red')
plt.axis('on')

#print( G.get_edge_data('B' , 'D'))

plt.show()
