#https://stackoverflow.com/questions/43442927/user-input-a-list-of-tuples/43443138
#https://stackoverflow.com/questions/961263/two-values-from-one-input-in-python
import cycle_fun
import networkx as nx
from re import findall

# Generates a list of nodes y1 to yi
def nodes_generator(nodes_no :int):
    nodes = []
    for i in range(nodes_no):
        nodes.append('y{}'.format(i+1))
    return nodes

def edge_str_to_tuples(edges_line:str):
    edges = []
    breakdown = findall('\(.*?,.*?\)', edges_line)
    for i in breakdown:
        edges.append(tuple([x for x in i[1:-1].split(',')]))
    return edges

def main():
    print("Welcome to SFG Slover ... CMD Version :)")
    print("We will solve the prolem step by step, using Mason Formula to get everything clear")

    G = nx.DiGraph()

    print('\n***Kindly Enter # of nodes of the graph in one  row ****')
    nodes_no = int(input())
    print('*** nodes *****')
    nodes = nodes_generator(nodes_no)
    print(nodes)
    G.add_nodes_from(nodes)

    print('Enter Edges in touples, ex : (y1,y2) , (y2,y3)....')
    edge_str = input()
    edges =edge_str_to_tuples(edge_str)
    G.add_edges_from(edge_str_to_tuples(edge_str))
    print(edges)

    s,t = input('Enter Start and End points form the SFG , ex: y1 y2\n').split()
    print('Start point = {} , End point = {}'.format(s,t))

    print("Now let's Solving")

    paths = list(nx.all_simple_paths(G,s,t))
    print('🔢🔢** \u2776 Forward Paths **')

    cycles = list(nx.simple_cycles(G));
    print('🔢🔢** \u2777  Cycles **')

if __name__ == '__main__':
    main()
# imp expression
#x = list(map(str,input().split()))
#print(x)






