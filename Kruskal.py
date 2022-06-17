def list_kruskal(G):
    return kruskal(G, list_get_edges(G))


def matrix_kruskal(G):
    return kruskal(G, matrix_get_edges(G))


def kruskal(G, E):
    total_cost = 0
    T = set()
    C, R = {u: u for u in range(G.vertices)}, {u: 0 for u in range(G.vertices)}  # Comp. reps and ranks
    for _, u, v in sorted(E):
        if find(C, u) != find(C, v):
            T.add((u, v))
            total_cost += G.edges[u][v]
            union(C, R, u, v)
    print(total_cost)
    return T


def list_get_edges(G):
    e = []
    for i in range(G.vertices):
        for key in G.edges[i]:
            e.append((G.edges[i][key], i, key))
    return e


def matrix_get_edges(G):
    e = []
    for u in range(G.vertices):
        for v in range(G.vertices):
            if G.edges[u][v] != 0:
                 e.append((G.edges[u][v], u, v))
    return e


def find(C, u):
    if C[u] != u:
        C[u] = find(C, C[u])  # Path compression
    return C[u]


def union(C, R, u, v):
    u, v = find(C, u), find(C, v)
    if R[u] > R[v]:  # Union by rank
        C[v] = u
    else:
        C[u] = v
    if R[u] == R[v]:  # A tie: Move v up a level
        R[v] += 1
