from coollections import deque

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
# why two dfs called ?

    def dfs(self,source):
        visited = [False]*self.v
        self.depthFirstSearch(visited,source)



    def depthFirstSearch(self,visited,source):
        print(source)
        visited[source] = True 
        for j in range(self.v):
            if(self.matrix[source][j] !=0 and not visited[j]):
                self.depthFirstSearch(visited,j)

                

        


















