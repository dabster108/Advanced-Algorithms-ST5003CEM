class DirectedGraphList:
    def __init__(self, num_vertices):
        self.v = num_vertices
        # List of neighbors for each vertex
        self.adj_list = [[] for _ in range(num_vertices)]

    def add_edge(self, source, destination):
        self.adj_list[source].append(destination)

    def print_graph(self):
        for i in range(self.v):
            print(f"{i} is connected to:", end=" ")
            for neighbor in self.adj_list[i]:
                print(neighbor, end=", ")
            print()


g_list = DirectedGraphList(6)
g_list.add_edge(0, 1)
g_list.add_edge(0, 2)
g_list.add_edge(1, 3)
g_list.print_graph()
