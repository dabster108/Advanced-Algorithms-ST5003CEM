class Graph:
    def __init__(self,v):
        self.matrix = [[0 for _ in range(v)] for _ in range(v)]
        self.v = v 

    def addEdge(self,source,destination):
        self.matrix[source][destination] = 1 
        self.matrix[destination][source] = 1 

    
    def printGraph(self):
        for i in range(len(self.matrix)):
            print(i , "is connected to", end=" ")
            for j in range(len(self.matrix)):
                if self.matrix[i][j]!=0:
                    print(j, end=" , ")
            print("")
    
g = Graph(6)
g.addEdge(0,1)
g.addEdge(0,2)
g.printGraph()



        

