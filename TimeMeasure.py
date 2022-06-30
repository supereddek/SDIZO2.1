from ListGraph import *
from Kruskal import *
from MatrixGraph import *
from BelmanFord import *
from Dijkstra import *
from Prim import *
import time

from ListGraph import *
from MatrixGraph import *
VERTICES = [25, 50, 75, 100, 150]
DENSITIES = [0.25, 0.50,  0.75, 0.99]


def prim():
    for dens in DENSITIES:
        for vert in VERTICES:
            prim_test_matrix(vert, dens)
    for dens in DENSITIES:
        for vert in VERTICES:
            prim_test_list(vert, dens)


def kruskal():
    for dens in DENSITIES:
        for vert in VERTICES:
            kruskal_test_matrix(vert, dens)
    for dens in DENSITIES:
        for vert in VERTICES:
            kruskal_test_list(vert, dens)


def dijkstra():
    for dens in DENSITIES:
        for vert in VERTICES:
            dijkstra_test_matrix(vert, dens)
    for dens in DENSITIES:
        for vert in VERTICES:
            dijkstra_test_list(vert, dens)


def bellman_ford():
    for dens in DENSITIES:
        for vert in VERTICES:
            bf_test_matrix(vert, dens)
    for dens in DENSITIES:
        for vert in VERTICES:
            bf_test_list(vert, dens)


def prim_test_matrix(vertices, density):
    mgraph = MatrixGraph()
    results = []
    with open("results.txt", "a") as res:
        res.write(f"Test for prim matrix with {vertices} vert and {density} density \n")
        for i in range(20):
            mgraph.generate_random_undirected(vertices, density)
            start = time.perf_counter_ns()
            matrix_prim(mgraph)
            stop = time.perf_counter_ns()
            results.append(stop - start)
            mgraph.clear()
        res.write(str(sum(results)/len(results) / 1000))                    # saves result in ms
        res.write("\n")


def prim_test_list(vertices, density):
    lgraph = ListGraph()
    results = []
    with open("results.txt", "a") as res:
        res.write(f"Test for prim list with {vertices} vert and {density} density \n")
        for i in range(50):
            lgraph.generate_random_undirected(vertices, density)
            start = time.perf_counter_ns()
            list_prim(lgraph)
            stop = time.perf_counter_ns()
            results.append(stop - start)
            lgraph.clear()
        res.write(str(sum(results) / len(results) / 1000))
        res.write("\n")


def kruskal_test_matrix(vertices, density):
    mgraph = MatrixGraph()
    results = []
    with open("results.txt", "a") as res:
        res.write(f"Test for kruskal matrix with {vertices} vert and {density} density \n")
        for i in range(20):
            mgraph.generate_random_undirected(vertices, density)
            start = time.perf_counter_ns()
            matrix_kruskal(mgraph)
            stop = time.perf_counter_ns()
            results.append(stop - start)
            mgraph.clear()
        res.write(str(sum(results)/len(results) / 1000))                    # saves result in ms
        res.write("\n")


def kruskal_test_list(vertices, density):
    mgraph = ListGraph()
    results = []
    with open("results.txt", "a") as res:
        res.write(f"Test for kruskal list with {vertices} vert and {density} density \n")
        for i in range(20):
            mgraph.generate_random_undirected(vertices, density)
            start = time.perf_counter_ns()
            list_kruskal(mgraph)
            stop = time.perf_counter_ns()
            results.append(stop - start)
            mgraph.clear()
        res.write(str(sum(results)/len(results) / 1000))                    # saves result in ms
        res.write("\n")


def dijkstra_test_matrix(vertices, density):
    mgraph = MatrixGraph()
    results = []
    with open("results.txt", "a") as res:
        res.write(f"Test for dijkstra matrix with {vertices} vert and {density} density \n")
        for i in range(20):
            mgraph.generate_random_undirected(vertices, density)
            start = time.perf_counter_ns()
            matrix_dijkstra(mgraph, 0, random.randint(0, vertices))
            stop = time.perf_counter_ns()
            results.append(stop - start)
            mgraph.clear()
        res.write(str(sum(results)/len(results) / 1000))                    # saves result in ms
        res.write("\n")


def dijkstra_test_list(vertices, density):
    mgraph = ListGraph()
    results = []
    with open("results.txt", "a") as res:
        res.write(f"Test for dijkstra list with {vertices} vert and {density} density \n")
        for i in range(20):
            mgraph.generate_random_undirected(vertices, density)
            start = time.perf_counter_ns()
            list_dijkstra(mgraph, 0, random.randint(0, vertices))
            stop = time.perf_counter_ns()
            results.append(stop - start)
            mgraph.clear()
        res.write(str(sum(results)/len(results) / 1000))                    # saves result in ms
        res.write("\n")

def bf_test_matrix(vertices, density):
    mgraph = MatrixGraph()
    results = []
    with open("results.txt", "a") as res:
        res.write(f"Test for bellman ford matrix with {vertices} vert and {density} density \n")
        for i in range(20):
            mgraph.generate_random_undirected(vertices, density)
            start = time.perf_counter_ns()
            matrix_bellman_ford(mgraph, 0, random.randint(0, vertices))
            stop = time.perf_counter_ns()
            results.append(stop - start)
            mgraph.clear()
        res.write(str(sum(results)/len(results) / 1000))                    # saves result in ms
        res.write("\n")


def bf_test_list(vertices, density):
    mgraph = ListGraph()
    results = []
    with open("results.txt", "a") as res:
        res.write(f"Test for bellman ford list with {vertices} vert and {density} density \n")
        for i in range(20):
            mgraph.generate_random_undirected(vertices, density)
            start = time.perf_counter_ns()
            list_bellman_ford(mgraph, 0, random.randint(0, vertices))
            stop = time.perf_counter_ns()
            results.append(stop - start)
            mgraph.clear()
        res.write(str(sum(results)/len(results) / 1000))                    # saves result in ms
        res.write("\n")
