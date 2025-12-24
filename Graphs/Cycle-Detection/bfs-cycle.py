from collections import deque

def bfs_cycle_detection(self, source):
    visited = [False] * self.v
    parent = [-1] * self.v
    q = deque()

    visited[source] = True
    q.append(source)

    while q:
        u = q.popleft()

        for v in range(self.v):
            if self.matrix[u][v] != 0:
                if not visited[v]:
                    visited[v] = True
                    parent[v] = u
                    q.append(v)
                elif parent[u] != v:
                    return True

    return False
