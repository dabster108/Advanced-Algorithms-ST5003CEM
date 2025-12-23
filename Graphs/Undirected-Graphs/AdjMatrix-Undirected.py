from collections import deque

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

    def bfs(self, start):
        """Return list of nodes in BFS order starting from `start`."""
        if start < 0 or start >= self.v:
            raise ValueError("start node out of range")
        visited = [False] * self.v
        order = []
        q = deque()
        visited[start] = True
        q.append(start)
        while q:
            node = q.popleft()
            order.append(node)
            for nbr in range(self.v):
                if self.matrix[node][nbr] and not visited[nbr]:
                    visited[nbr] = True
                    q.append(nbr)
        return order

if __name__ == "__main__":
    g = Graph(6)
    g.addEdge(0,1)
    g.addEdge(0,2)
    g.addEdge(1,3)
    g.addEdge(2,4)
    g.addEdge(4,5)
    g.printGraph()
    print("BFS from 0:", g.bfs(0))



        

