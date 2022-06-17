class ListGraph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = [{} for _ in range(vertices)]

    def add_edge(self, source, destination, weight):
        self.edges[source][destination] = weight
        self.edges[destination][source] = weight

    def add_edge_directed(self, source, destination, weight):
        self.edges[source][destination] = weight


    #todo optimize
    def make_from_file_directed(self):
        with open('numbers.txt') as f:
            edges, vertices = [int(x) for x in f.readline().split()]  # read first line
            self.vertices = vertices
            self.edges = [{} for _ in range(vertices)]
            for line in f.readlines():  # read rest of lines
                u, v, w = [int(x) for x in line.split()]
                self.add_edge_directed(u, v, w)

    #todo optimize
    def make_from_file_undirected(self):
        with open('numbers.txt') as f:
            edges, vertices = [int(x) for x in f.readline().split()]  # read first line
            self.vertices = vertices
            self.edges = [{} for _ in range(vertices)]
            for line in f.readlines():  # read rest of lines
                u, v, w = [int(x) for x in line.split()]
                self.add_edge(u, v, w)

    # todo
    def print(self):
        for i in range(len(self.edges)):
            for key in self.edges[i]:
                print("%d -> %d weight: %d" % (i, key, self.edges[i][key]))
