class Graph:
    def __init__(self,v):
        self.v = v 
        self.adjList = [[] for _ in range(v)]
        
    def addEdge(self,source,destination):
        self.adjList[source].append(destination)
        self.adjList[destination].append(source)

    def printGraph(self):
        for i in range(len(self.adjList)):
            print(i , "is connected to", end=" ")
            for j in self.adjList[i]:
                print(j, end=" , ")
            print("")

g = Graph(6)
g.addEdge(0,1)
g.addEdge(0,2)
g.printGraph()
