# https://stackoverflow.com/questions/6499327/the-pythonic-way-to-generate-pairs
#https://stackoverflow.com/questions/10202938/how-do-i-use-method-overloading-in-python
from typing import List, Any, Tuple

import networkx as nx
import matplotlib.pyplot as plt
import itertools
from functools import reduce

# Creating a digraph

G = nx.DiGraph()

# Adding a list of Nodes :
G.add_nodes_from(["y1", "y2", "y3", "y4", "y5"])

# adding a list of edges :

G.add_edges_from(
    [("y1", "y2"), ("y2", "y3"), ("y3", "y4"), ("y4", "y5"), ("y3", "y5"), ("y5", "y1"), ("y4", "y2"), ("y5", "y3"),
     ('y1', 'y1')])

# Return a list of cycles (even self loops):

cy = list(nx.simple_cycles(G))

# getting forward paths : start and end points are required
p = list(nx.all_simple_paths(G, "y1", "y5"))

print(p)
print("cycles R :")
print(cy)

# trying getting possible combinations
stuff = [1, 2, 3]
for L in range(0, len(stuff) + 1):
    for subset in itertools.combinations(stuff, L):
        print(subset)


# trying to separate cycles into edges :
# done @ 23:32 9/9/2018 :
def cycle_to_edge(x: list):
    len = x.__len__();
    edges: List[Tuple[Any, Any]] = []
    print(len)

    if len == 1 :
        print("({} , {})".format(x[0] , x[0]))
        edges.append((x[0] ,x[0]))
    elif len < 0 :
        print('Invalid Cycle')
    elif len == 2:
        print('({} , {})'.format(x[0],x[1]))
        edges.append((x[0] ,x[1]))
    else:
        for i in range(len-1):
            print('({} , {})'.format(x[i],x[i+1]))
            edges.append((x[i] ,x[i+1]))

        print('({} , {})'.format(x[len-1],x[0]))
        edges.append((x[len-1] ,x[0]))

    return edges



edge_of_cy = cycle_to_edge(cy[1])
print('edges of cycle 1 :' + str(edge_of_cy))
for i in cy:
    cycle_to_edge(i)
    print('****')

print('>>>>>><<<<<<<')
print(set(cy[0]).intersection(cy[1]))

print(cy.__len__())

# creates a list containing number of loops to get combinations between 'em
def loop_num_list(cycles_no):
    combin = []
    for i in range(cycles_no):
        combin.append(i);
    return combin

# get list of combinations for(2 , 3 ,4 ....)
def get_loop_comb(loop_num:list,no_of_loops:int):
    pairs = []
    for pair in itertools.combinations(loop_num,no_of_loops):
        pairs.append(pair)
    return pairs

def get_loop_combin(cy_no,no_of_loops:int,loops:list):
    pairs = []
    loop_num = loop_num_list(cy_no)
    for pair in itertools.combinations(loop_num,no_of_loops):
        pairs.append((loops[pair[0]],loops[pair[1]]))
    return pairs


lo_num = loop_num_list(5);
print(lo_num)

combinations_cy = get_loop_comb(lo_num, 3)

loops_com = get_loop_combin(5,2,cy)
print('//////////////////')
print(loops_com)
print('/////////////////')
print(combinations_cy)


d = [(1, 2, 3, 4), (2, 3, 4), (3, 4, 5, 6, 7)]


inter = list(reduce(set.intersection, [set(item) for item in loops_com[0]]))

print(inter)



