def list_kruskal(graph):
    return kruskal(graph, list_get_edges(graph))


def matrix_kruskal(graph):
    return kruskal(graph, matrix_get_edges(graph))


def kruskal(graph, edges):
    total_cost = 0
    tree = set()
    groups = {u: u for u in range(graph.vertices)}      # every group representative points to itself
    ranks = {u: 0 for u in range(graph.vertices)}
    for _, u, v in sorted(edges):
        if find(groups, u) != find(groups, v):
            tree.add((u, v))
            total_cost += graph.edges[u][v]
            union(groups, ranks, u, v)
    print(total_cost)
    return tree


def list_get_edges(graph):
    edges = []
    for i in range(graph.vertices):
        for key in graph.edges[i]:
            edges.append((graph.edges[i][key], i, key))
    return edges


def matrix_get_edges(graph):
    edges = []
    for u in range(graph.vertices):
        for v in range(graph.vertices):
            if graph.edges[u][v] != 0:
                edges.append((graph.edges[u][v], u, v))
    return edges


def find(groups, u):
    if groups[u] != u:
        groups[u] = find(groups, groups[u])  # Path compression
    return groups[u]


def union(groups, ranks, u, v):
    u, v = find(groups, u), find(groups, v)
    if ranks[u] > ranks[v]:  # Union by rank
        groups[v] = u
    else:
        groups[u] = v
    if ranks[u] == ranks[v]:  # A tie: Move v up a level
        ranks[v] += 1
