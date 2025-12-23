from collections import deque
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

    def bfs(self, source):
        visited = [False] * self.v
        q = deque()

        q.append(source)           # start node
        visited[source] = True

        while q:
            node = q.popleft()     # remove front
            print(node)

            for neighbor in self.adjList[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    q.append(neighbor)
    


    def dfs(self, source):
        visited = [False] * self.v
        self._dfsUtil(source, visited)

    def _dfsUtil(self, node, visited):
        print(node)
        visited[node] = True

        for neighbor in self.adjList[node]:
            if not visited[neighbor]:
                self._dfsUtil(neighbor, visited)





g = Graph(6)
g.addEdge(0,1)
g.addEdge(0,2)
g.printGraph()




# TRAVERSE - THING 
