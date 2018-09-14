# https://stackoverflow.com/questions/6499327/the-pythonic-way-to-generate-pairs
#https://stackoverflow.com/questions/10202938/how-do-i-use-method-overloading-in-python
#https://stackoverflow.com/questions/1708510/python-list-vs-tuple-when-to-use-each
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
    [("y1", "y2"), ("y2", "y3"), ("y3", "y4"), ("y4", "y5"), ("y5", "y3"), ("y5", "y1"), ("y4", "y2") ,('y1','y1')])

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

#//////////////////// 2) functions used //////////////////// :

# trying to separate cycles into edges : (all right) >> BUT mind invalid cycles
# done @ 23:32 9/9/2018 :
def cycle_to_edge(x: list):
    len = x.__len__();
    edges: List[Tuple[Any, Any]] = []
    #print(len)

    if len == 1 :
        #print("({} , {})".format(x[0] , x[0]))
        edges.append((x[0] ,x[0]))
    elif len < 0 :
        print('Invalid Cycle')
    elif len == 2:
        #print('({} , {})'.format(x[0],x[1]))
        edges.append((x[0] ,x[1]))
    else:
        for i in range(len-1):
            #print('({} , {})'.format(x[i],x[i+1]))
            edges.append((x[i] ,x[i+1]))

        #print('({} , {})'.format(x[len-1],x[0]))
        edges.append((x[len-1] ,x[0]))

    return edges


# creates a list containing number of indexes of loops to get combinations between 'em later : Simple enough to be right
def loop_num_list(cycles_no):
    combin = []
    for i in range(cycles_no):
        combin.append(i);
    return combin


# converting list of indexes into a list of cycles or whatever:
def index_to_list(indexes:list , take:tuple):
    converted = []
    for i in range(indexes.__len__()):
        converted.append(take[indexes[i]])
    return converted



# get list of combinations for (1,2,3,4,...)loops
def get_loop_combin(loops_list:list , no_of_loops):
    """ this function gets list of combinations for (1,2,3,...) loops """
    tuples = []
    if(no_of_loops ==1):
        return loops_list
    else:
      for tup in itertools.combinations(loops_list, no_of_loops):
          tuples.append(tup)
      return tuples


# see if combinations of loops are intersected, if so, it returns intersection!!! else returns false
def is_intersected(loops_com):
        inter = list(reduce(set.intersection, [set(item) for item in loops_com]))
        return inter if inter.__len__()>0 else False
# see if the loop is intersected with the path;returns true/false
def is_intersected(path:list , loop:list):
    return True if set(path)&set(loop)  else False

#returns a list containing tuples of intersected loops
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
    return method_two if method_two.__len__() !=0 else False


# gets intersection between a path and a loop; returns list of loops intersected with this path
def get_intersected_loops_to_path(path:list, loops:list):
    intersected = []
    for i in range(loops.__len__()):
        #print(set(path)&set(loops[i]))
        if(is_intersected(path,loops[i])):intersected.append(loops[i])
    return intersected if intersected.__len__() !=0 else False

def get_max_loop_intersection(loops:list):
    """ computes max loops required by getting intersection for each loop_no"""
    max = 0
    for i in range (1,7):
        if get_intersected(get_loop_combin(loops ,i)) !=False:
            max+=1
    return max


d = [(1, 2, 3, 4), (2, 3, 4), (3, 4, 5, 6, 7)]



'''
trial_loop_com = list(itertools.combinations(range(6), 3))
print(trial_loop_com)

'''

# Getting edges of cyles:
print('****edges of cycles****')
for i in cy :
    print(cycle_to_edge(i))
# loop_num :
print('***loop_num_list trial***')
lnc = loop_num_list(3)
print(lnc)

# get_loop_combin :
print('***get_loop_combine***')
loop_com = get_loop_combin(cy,4)
print(loop_com)

# get_intersected:
print('***get_intersected***')
gin= get_intersected(loop_com)
print(get_intersected(loop_com))

# get_intersected_loops_to_path
print("***get_intersected_loops_to_path***")
print(get_intersected_loops_to_path(p[0],cy))

# get_max_loop_intersection
print('***get_max_loop_intersection***')
print(get_max_loop_intersection(cy))
nodes = ['y1' , 'y2','y3','y4','y5']

print(nodes)
