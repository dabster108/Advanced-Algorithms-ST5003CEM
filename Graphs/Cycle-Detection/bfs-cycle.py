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
                # If not visited, push to queue
                if not visited[v]:
                    visited[v] = True
                    parent[v] = u
                    q.append(v)

                # If visited and NOT parent → cycle
                elif parent[u] != v:
                    return True

    return False
