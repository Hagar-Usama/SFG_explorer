import networkx as nx

'''

G = nx.MultiGraph() # or MultiDiGraph
G.add_edge(0,1,key='a',weight=7)
G[0][1]['a']  # key='a' {'weight': 7}

G[0][1]['a']['weight'] = 10


'''
G = nx.MultiGraph()
G.add_path(['a' , 'b' , 'c' , 'd'])
y = G.get_edge_data('a','b')



print(y)
