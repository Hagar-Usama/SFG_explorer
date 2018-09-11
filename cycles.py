# https://stackoverflow.com/questions/6499327/the-pythonic-way-to-generate-pairs
#https://stackoverflow.com/questions/10202938/how-do-i-use-method-overloading-in-python
from typing import List, Any, Tuple
import networkx as nx
import itertools
from functools import reduce

# ////// 1) Creating a digraph //////////////

G = nx.DiGraph()

# Adding a list of Nodes :
G.add_nodes_from(["y1", "y2", "y3", "y4", "y5"])

# adding a list of edges :

G.add_edges_from(
    [("y1", "y2"), ("y2", "y3"), ("y3", "y4"), ("y4", "y5"), ("y5", "y3"), ("y5", "y1"), ("y4", "y2")])

# Return a list of cycles (even self loops):

cy = list(nx.simple_cycles(G))

# getting forward paths : start and end points are required
print('***Forward paths*** :')
p = list(nx.all_simple_paths(G, "y1", "y5"))

#///////////////Digraph created/////////////////////////

# printing paths and cycles:
print(p)
print('***Cycles*** :')
print(cy)

# trying getting possible combinations
'''

stuff = [1, 2, 3]
for L in range(0, len(stuff) + 1):
    for subset in itertools.combinations(stuff, L):
        print(subset)


'''


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


# creates a list containing number of loops to get combinations between 'em
def loop_num_list(cycles_no):
    combin = []
    for i in range(cycles_no):
        combin.append(i);
    return combin

# get list of combinations for(2 , 3 ,4 ....)
def get_loop_combin(no_of_loops:int,loops:list):
    pairs = []
    cy_no = loops.__len__()
    loop_num = loop_num_list(cy_no)
    for pair in itertools.combinations(loop_num,no_of_loops):
        pairs.append((loops[pair[0]],loops[pair[1]]))
    return pairs


def is_intersected(loops_com):
        inter = list(reduce(set.intersection, [set(item) for item in loops_com]))
        return inter if inter.__len__()>0 else False

def get_intersected(loops_com:list):
    intersected = []
    '''
    
    even_indices = [i for i, elem in loops_com if (is_intersected(elem)) != False]
    print("Even_ind")
    print(even_indices)

    print(even_indices.__len__())
    
    '''

    method_two = []
    for i in range(loops_com.__len__()):
        inter = list(reduce(set.intersection, [set(item) for item in loops_com[i]]))
        if inter.__len__() != 0 : #if there is an intersection
            method_two.append(loops_com[i])

    #print("Method Two")
    #print(method_two.__len__())
    #print(method_two)
    return method_two




d = [(1, 2, 3, 4), (2, 3, 4), (3, 4, 5, 6, 7)]


'''
trial_loop_com = list(itertools.combinations(range(6), 3))
print(trial_loop_com)

'''

