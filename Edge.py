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
