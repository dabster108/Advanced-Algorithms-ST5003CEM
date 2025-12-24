def dfs_cycle_detection(self, u, visited, parent):
    visited[u] = True

    for v in range(self.v):
        if self.matrix[u][v] != 0:
            if not visited[v]:
                if self.dfs_cycle_detection(v, visited, u):
                    return True

            elif v != parent:
                return True

    return False
