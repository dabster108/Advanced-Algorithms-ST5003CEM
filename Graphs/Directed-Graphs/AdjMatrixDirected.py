class DirectedGraphMatrix:
    def __init__(self, num_vertices):
        self.v = num_vertices
        self.matrix = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]

    def add_edge(self, source, destination):
        self.matrix[source][destination] = 1

    def print_graph(self):
        for i in range(self.v):
            print(f"{i} is connected to:", end=" ")
            for j in range(self.v):
                if self.matrix[i][j] == 1:
                    print(j, end=", ")
            print()

g_matrix = DirectedGraphMatrix(6)
g_matrix.add_edge(0, 1)
g_matrix.add_edge(0, 2)
g_matrix.add_edge(1, 3)
g_matrix.print_graph()
