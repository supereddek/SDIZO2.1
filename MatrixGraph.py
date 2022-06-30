from math import floor
import random

import pandas as pd


class MatrixGraph:
    def __init__(self, vertices = 0):
        self.vertices = vertices
        self.edges = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def add_edge(self, source, destination, weight):
        self.edges[source][destination] = weight
        self.edges[destination][source] = weight

    def add_edge_directed(self, source, destination, weight):
        self.edges[source][destination] = weight

    def make_from_file_undirected(self):
        with open('numbers.txt') as f:
            edges, vertices = [int(x) for x in f.readline().split()]  # read first line
            self.vertices = vertices
            self.edges = [[0 for _ in range(vertices)] for _ in range(vertices)]
            for line in f.readlines():  # read rest of lines
                u, v, w = [int(x) for x in line.split()]
                self.add_edge(u, v, w)

    def make_from_file_directed(self):
        with open('numbers.txt') as f:
            edges, vertices = [int(x) for x in f.readline().split()]  # read first line
            self.vertices = vertices
            self.edges = [[0 for _ in range(vertices)] for _ in range(vertices)]
            for line in f.readlines():  # read rest of lines
                u, v, w = [int(x) for x in line.split()]
                self.add_edge_directed(u, v, w)

    def generate_random_undirected(self, vertices, density):
        self.vertices = vertices
        self.edges = [[0 for _ in range(vertices)] for _ in range(vertices)]
        # calculate edges based on density
        required_edges = floor((vertices * (vertices - 1) * density) / 2)
        if required_edges < self.vertices:
            print("fToo few edges to create connected graph."
                  f"Making {vertices} edges instead.")
            required_edges = vertices
        # generates spanning tree to make sure that every vertex is connected
        connected = {0}
        for u in range(1, vertices):
            self.add_edge(random.choice(tuple(connected)), u, random.randint(0, 20))
            connected.add(u)
        required_edges -= self.vertices
        free_k = {x for x in range(vertices)}
        while required_edges != 0:
            # select k from list
            k = random.choice(list(free_k))
            # select v making sure uv doesn't already exist
            v = random.choice(list(set([x for x in range(0, vertices)])
                                   - set([i for i, e in enumerate(self.edges[k]) if e != 0]) - {k}))
            self.add_edge(k, v, random.randint(0, 20))
            if len([i for i, e in enumerate(self.edges[k]) if e != 0]) == self.vertices - 1:
                free_k.remove(k)
            if len([i for i, e in enumerate(self.edges[v]) if e != 0]) == self.vertices - 1:
                free_k.remove(v)
            required_edges -= 1

    def generate_random_directed(self, vertices, density):
        self.vertices = vertices
        self.edges = [[0 for _ in range(vertices)] for _ in range(vertices)]
        # calculate edges based on density
        required_edges = floor((vertices * (vertices - 1) * density))
        if required_edges < self.vertices:
            print("fToo few edges to create connected graph."
                  f"Making {vertices} edges instead.")
            required_edges = vertices
        # generates spanning tree to make sure that every vertex is connected
        connected = {0}
        for u in range(1, vertices):
            self.add_edge(random.choice(tuple(connected)), u, random.randint(0, 20))
            connected.add(u)
        required_edges -= self.vertices
        free_k = {x for x in range(vertices)}
        while required_edges != 0:
            # select k from list
            k = random.choice(list(free_k))
            # select v making sure uv doesn't already exist
            v = random.choice(list(set([x for x in range(0, vertices)])
                                   - set([i for i, e in enumerate(self.edges[k]) if e != 0]) - {k}))
            self.add_edge(k, v, random.randint(0, 20))
            if len([i for i, e in enumerate(self.edges[k]) if e != 0]) == self.vertices - 1:
                free_k.remove(k)
            required_edges -= 1

    def print(self):
        print(pd.DataFrame(self.edges))
        print()

    def clear(self):
        self.edges = []
        self.vertices = 0