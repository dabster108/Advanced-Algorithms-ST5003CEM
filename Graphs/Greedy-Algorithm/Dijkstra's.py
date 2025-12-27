class Graph:
    def __init__(self, v):
        self.v = v
        self.matrix = [[0 for _ in range(v)] for _ in range(v)]

    def addEdge(self, u, v, w):
        self.matrix[u][v] = w
        self.matrix[v][u] = w   

    def findMinVertex(self, dist, visited):
        min_vertex = -1
        for i in range(self.v):
            if not visited[i] and (min_vertex == -1 or dist[i] < dist[min_vertex]):
                min_vertex = i
        return min_vertex

    def dijkstra(self, source):
        dist = [float('inf')] * self.v
        prevpath = [-1] * self.v
        visited = [False] * self.v

        dist[source] = 0

        for i in range(self.v):
            minvertex = self.findMinVertex(dist, visited)
            visited[minvertex] = True

            for j in range(self.v):
                if self.matrix[minvertex][j] != 0 and not visited[j]:
                    newDist = dist[minvertex] + self.matrix[minvertex][j]
                    if newDist < dist[j]:
                        dist[j] = newDist
                        prevpath[j] = minvertex

        return dist, prevpath