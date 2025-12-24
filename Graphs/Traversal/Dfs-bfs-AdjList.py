from collections import deque

class Graph:
    def __init__(self, v):
        self.v = v
        self.adjList = [[] for _ in range(v)]

    def addEdge(self, source, destination):
        self.adjList[source].append(destination)
        self.adjList[destination].append(source)  # undirected graph

    def printGraph(self):
        for i in range(self.v):
            print(i, "is connected to", self.adjList[i])

    def bfs(self, source):
        """Breadth First Search using adjacency list"""
        visited = [False] * self.v
        q = deque()

        q.append(source)
        visited[source] = True

        while q:
            x = q.popleft()
            print(x)

            for neighbor in self.adjList[x]:
                if not visited[neighbor]:
                    q.append(neighbor)
                    visited[neighbor] = True

    def dfs(self, source):
        visited = [False] * self.v
        self.depthFirstSearch(source, visited)

    def depthFirstSearch(self, source, visited):
        print(source)
        visited[source] = True

        for neighbor in self.adjList[source]:
            if not visited[neighbor]:
                self.depthFirstSearch(neighbor, visited)
