from collections import deque


class Graph:
    def __init__(self,v):
        self.matrix = [[0 for _ in range(v)] for _ in range(v)]
        self.v = v

    def addEdge(self,source,destination,w):
        self.matrix[source][destination] = w
        self.matrix[destination][source] = 1

    def printGraph(self):
        for i in range(len(self.matrix)):
            print(i , "is connected to", end=" ")
            for j in range(len(self.matrix)):
                if self.matrix[i][j]!=0:
                    print(j, end=" , ")
            print("")

    def bfs(self, source):
        """Breadth-first traversal on adjacency matrix starting from `source`."""
        q = deque()
        visited = [False] * self.v
        q.append(source)
        visited[source] = True
        while q:
            x = q.dequeue()
            print(x)
            for j in range(self.v):
                if self.matrix[x][j] != 0 and not visited[j]:
                    q.append(j)
                    visited[j] = True


    def dijakstra(self,source,destination):
        dist = [float('inf')]*self.v
        prevpath = [-1]*self.v
        visited = [False]*self.v
        dist[source] = 0
        for i in range(self.v):
            minvertex = self.findMinVertex(dist,visited)
            visited[minvertex] = True
            for j in range(self.v):
                if self.matrix[minvertex][j] != 0 and not visited[j]:
                    if dist[minvertex] + self.matrix[minvertex][j] < dist[j]:
                        dist[j] = dist[minvertex] + self.matrix[minvertex][j]
                        prevpath[j] = minvertex
                        
# algorithm to find path

        

        
    def findMinVertext(self,dist,visited):
        #we give max value to minimum 
        min = -1
        for i in range(len(dist)):
           if((min == -1 or dist[i] < min) and not visited[i]):
                min = dist[i]
        return min 

    

            

    


    def dfs(self,source):
        visited = [False]*self.v
        self.depthFirstSearch(visited,source)

    def depthFirstSearch(self,visited,source):
        print(source)
        visited[source] = True 
        for j in range(self.v):
            if(self.matrix[source][j] !=0 and not visited[j]):
                self.depthFirstSearch(visited,j)
                

        

g = Graph(6)
g.addEdge(0,1,10)
g.addEdge(0,5,20)
g.addEdge(1,2,3)
g.addEdge(1,4,7)
g.addEdge(2,3,2)
g.addEdge(3,4,10)
g.addEdge(3,5,15)
g.addEdge(4,5,4)
g.printGraph()
















