import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
G = nx.dodecahedral_graph()
pos = nx.spring_layout(G)
ax = plt.gca()
for u,v in G.edges():
    x = [pos[u][0],pos[v][0]]
    y = [pos[u][1],pos[v][1]]
    l = Line2D(x,y,linewidth=8,solid_capstyle='round')
    ax.add_line(l)
ax.autoscale()
plt.show()
