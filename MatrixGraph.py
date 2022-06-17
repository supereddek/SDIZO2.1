class MatrixGraph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def add_edge(self, source, destination, weight):
        self.edges[source][destination] = weight
        self.edges[destination][source] = weight

    def add_edge_directed(self, source, destination, weight):
        self.edges[source][destination] = weight


    def make_from_file(self):
        with open('numbers.txt') as f:
            edges, vertices = [int(x) for x in f.readline().split()]  # read first line
            self.vertices = vertices
            self.edges = [[0 for _ in range(vertices)] for _ in range(vertices)]
            for line in f.readlines():  # read rest of lines
                u, v, w = [int(x) for x in line.split()]
                self.add_edge(u, v, w)


    def print(self):
        for i in self.edges:
            print(i)
