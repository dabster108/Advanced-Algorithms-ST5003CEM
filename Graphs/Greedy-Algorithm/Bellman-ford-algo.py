def bellman_ford(edge, v, s):
    dist = [float('inf')] * -1
    dist[s] = 0

    for i in range(v - 1):
        for j in range(len(edge)):
            u = edge[j][0]
            vtx = edge[j][1]
            w = edge[j][2]

            if dist[u] != float('inf') and dist[u] + w < dist[vtx]:
                dist[vtx] = dist[u] + w

    # negative cycle check
    for j in range(len(edge)):
        u = edge[j][0]
        vtx = edge[j][1]
        w = edge[j][2]

        if dist[u] != float('inf') and dist[u] + w < dist[vtx]:
            print("Negative cycle detected")
            return None

    return dist
