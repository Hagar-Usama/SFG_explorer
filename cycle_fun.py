from typing import List, Any, Tuple
import networkx as nx
import itertools
from functools import reduce

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


'''
# get list of combinations for(2 , 3 ,4 ....)loops
def get_loop_combin(no_of_loops:int,loops:list):
    pairs = [] # maybe name isn't describtive >> change it to tuple
    cy_no = loops.__len__()
    if(no_of_loops == 1 ):
        return loops
    else:
        loop_num = loop_num_list(cy_no)
    for pair in itertools.combinations(loop_num,no_of_loops):
          pairs.append(index_to_list(pair,loops))
    return pairs


'''


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
    return method_two


# gets intersection between a path and a loop; returns list of loops intersected with this path
def get_intersected_loops_to_path(path:list, loops:list):
    intersected = []
    for i in range(loops.__len__()):
        #print(set(path)&set(loops[i]))
        if(is_intersected(path,loops[i])):intersected.append(loops[i])
    return intersected if intersected.__len__() !=0 else False
