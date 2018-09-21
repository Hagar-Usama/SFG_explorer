# https://stackoverflow.com/questions/6499327/the-pythonic-way-to-generate-pairs
#https://stackoverflow.com/questions/10202938/how-do-i-use-method-overloading-in-python
#https://stackoverflow.com/questions/1708510/python-list-vs-tuple-when-to-use-each
#https://stackoverflow.com/questions/209840/convert-two-lists-into-a-dictionary-in-python
#https://docs.sympy.org/latest/tutorial/manipulation.html

import itertools
from functools import reduce
from typing import List, Any, Tuple, Union
import networkx as nx
from sympy import symbols as syms, simplify, Symbol

# ////// 1) Creating a digraph //////////////

G = nx.DiGraph()

# Adding a list of Nodes :
G.add_nodes_from(["y1", "y2", "y3", "y4", "y5"])

# adding a list of edges :
y1 ,y2,y3,y4,y5 = syms('y1 y2 y3 y4 y5')

G.add_edges_from(
    [('y1' , 'y2'), ("y2", "y3"), ("y3", "y4"), ("y4", "y5"), ("y5", "y3"), ("y5", "y1"), ("y4", "y2") ,('y1','y1')])



# Values of edges:
val = ['g1','g2','g3','g4',-1,'h1','h2','h3']
symbols = [G.edges.__len__()]


print('******edges*****')
print(G.edges)


edges_dict =  dict(zip(G.edges, val))

print('******edges values *****')
print(edges_dict)

print("***dict it***")
print(edges_dict[('y1','y2')])

sy = syms('x'); y= syms('y')


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
def symbolize(edge_val:list):
    """converts a list of strings to symbols"""
    sym_list = []
    for i in edge_val:
        if type(i) == int: #might be double float !!
            sym_list.append(i)
        else:
            x= syms(i)
            sym_list.append(x)
    return sym_list

# trying to separate cycles into edges : (all right) >> BUT mind invalid cycles
# done @ 23:32 9/9/2018 :

def cycle_to_edge(x: list):
    len = x.__len__();
    edges: List[Tuple[Any, Any]] = []
    #print(len)

    if len == 1 :
        edges.append((x[0] ,x[0]))
    elif len < 0 :
        print('Invalid Cycle')
    elif len == 2:
         edges.append((x[0] ,x[1]))
    else:
        for i in range(len-1):
             edges.append((x[i] ,x[i+1]))
        edges.append((x[len-1] ,x[0]))

    return edges


def cycle_to_edge_val(x: list , val:dict):
    len = x.__len__();
    mod = []

    if len == 1 :
        mod.append(val[(x[0] ,x[0])])
    elif len < 0 :
        print('Invalid Cycle')
    elif len == 2:
        mod.append(val[(x[0] ,x[1])])
    else:
        for i in range(len-1):
            mod.append(val[(x[i] ,x[i+1])])
        mod.append(val[(x[len-1] ,x[0])])

    return product_sym(symbolize(mod))


def tup_cycle_to_edge_val(loops:list , val:dict):
    edges = []
    for loop in loops:
        edges.append(cycle_to_edge_val(loop , val))
    return tuple(edges)


def list_tup_edge_val(loops:list , val:dict):
    edges = []
    for loop in loops:
        edges.append(tup_cycle_to_edge_val(loop , val))
    return (edges)

def big_list_edge_val(loops:list , val:dict):
    edges = []
    indi_loops = loops[0]
    first_cycle = []
    #print(indi_loops)
    for loop in indi_loops:
        #print(loop)
        first_cycle.append(cycle_to_edge_val(loop , val))
    edges.append(first_cycle)

    for i in range(1, loops.__len__()):
        edges.append(list_tup_edge_val(loops[i] , val))
    return edges


def loop_cycle_to_edge_val(loops:list , val:dict):

    pass


def loop_cycle_to_edge(loops:list):
    """ takes a list of cycles and covert them into edges"""
    edges = []
    for loop in loops:
        edges.append(cycle_to_edge(loop))
    return edges

def get_edge_val(edges:list , edges_dictionary:dict):
    edges_val = []
    pass

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
        return tuple(loops_list)
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
            print("__________Method 2_{}____________".format(i))
            print(loops_com[i])


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
    inter_loops = []
    for i in range (1,7):
        g_inter = get_intersected(get_loop_combin(loops ,i))
        if g_inter !=False:
            max+=1
            inter_loops.append(g_inter)
    return [max , inter_loops]

def product_sym(loop:list):
    """ returns the products of a list:cycle of symbols """
    mul_list = []
    if loop.__len__() == 1:
        return loop[0]
    else:
        product = 1
        for element in loop:
            product *=element
        mul_list.append(product)
        return product



d = [(1, 2, 3, 4), (2, 3, 4), (3, 4, 5, 6, 7)]

def product_tup(loops:list):
    """ multiplies each element in a tuple by each other
       EX : [(g3*g4*h1, -g1*g3*g4*h3), (g3*g4*h1, -g4*h2), (-g1*g3*g4*h3, -g4*h2), (-g1*g3*g4*h3, g2)]>>
       [-g1*g3**2*g4**2*h1*h3, -g3*g4**2*h1*h2, g1*g3*g4**2*h2*h3, -g1*g2*g3*g4*h3]
    """
    mul_edges = []
    for loop in loops:
        mul_edges.append(product_sym(loop))
    return mul_edges

def big_product(loops:list):
    mul_edges = []
    mul_edges.append(loops[0])
    if(loops.__len__()>1):
        for i in range(1,loops.__len__()):
            mul_edges.append(product_tup(loops[i]))
        return mul_edges

def sym_sum(loops:list):
    """ gets summation of a list of symbols"""
    sum = 0
    if(loops.__len__() == 1):
        return loops[0]
    else:
        for loop in loops:
            sum +=loop
    return sum

def add_sym(loops:list):
    final_edges = []
    for loop in loops:
        final_edges.append(sym_sum(loop))
    return final_edges
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
loop_com = get_loop_combin(cy,3)
print(loop_com)

# get_intersected:
print('\n***get_intersected***')
gin= get_intersected(loop_com)
print(get_intersected(loop_com))

# get_intersected_loops_to_path
print("***get_intersected_loops_to_path***")
print(get_intersected_loops_to_path(p[0],cy))

# get_max_loop_intersection
print('***get_max_loop_intersection***')
[max , inter_loops] = get_max_loop_intersection(cy)
nodes = ['y1' , 'y2','y3','y4','y5']
print (max)
#print(inter_loops)
for i in range(0,inter_loops.__len__()):
   print(inter_loops[i])
   print('***********')

print(list_tup_edge_val(inter_loops[1], edges_dict))
print('*********///')
print('list of values')
#print(cycle_to_edge_val(cy[2], edges_dict))
#print(tup_cycle_to_edge_val(cy , edges_dict))


print('>>>>>>><<<<<<<<<<<<<<<')

kk = inter_loops[0]
print(kk[0])


print('*****big******')
big = big_list_edge_val(inter_loops,edges_dict)
for b in big :
    print(b)
print('********************************end of big***************************************************')


print(product_tup(big[1]))

print("&&&&&&&&&&&&&&&&")
bbig = big_product(big)
for b in bbig:
    print(b)

print('ooooooooooooooooooooooooooooooooooooooooooooooooo')
bef_last = add_sym(bbig)
print(bef_last) # form before last

def list_generator(max:int):
    """ generates a list of numbers from 0 to max """
    num_list = []
    for i in range (1,max+1):
        num_list.append(i)
    return num_list

def get_delta(loops:list):
    nums = list_generator(loops.__len__())
    delta =list(map(lambda x, y: x *(-1)**y, loops, nums))
    return 1-delta[0]

print(get_delta(bef_last))
uu = [1,5,4]
mully = reduce(lambda x, y: x * y, uu, 1)
print('mully')
print(mully)


"""
jx = big[0]
print(jx[0])
ui= product_sym(jx[0])
uj = product_sym(jx[1])
print(ui)
print(uj)
print(ui*uj)
print(simplify(ui*uj))

"""

