# 9/8/2018 >> project started on 8/8/2018
# if 2 edges have the start and end : this unacceptable >>instead let
# g = g1 + g2 with one arrow
class Edge:
    num_of_edges = 0
    def __init__(self , start , end , value):
        self.start = start
        self.end = end
        self.value = value

        Edge.num_of_edges += 1

    def getValue(self,start , end):
        return self.value

    def isTheEdge(self,start ,end):
        if((self.start == start) and(self.end ==end)):
            print("Edge already exists")
            print("The Edge value is : " + self.value)
            return True
        else:
            print("not such an Edge!")
            return False

ed = Edge('y1','y2','g1')
ed2 = Edge('y1','y3','h1')
ed3= Edge('y1','y4','g5')
my_edges = []
my_edges.append(ed)
my_edges.append(ed2)
my_edges.append(ed3)
my_edges.append(Edge('y1' ,'y5','-1'))

x =my_edges[3]
print(x.value)

# Use format for final answer :)
print('{}x{}'.format(ed.start , ed.end))

# getting value :
e = Edge.getValue(ed ,'y1', 'y3')
print("e is " + e)
print(ed.value)

x = ed.isTheEdge('y2', 'y1')
print(x)
