from heapq import heappop, heappush


# todo optimize
def list_prim(G, s):
    P, Q = {}, [(0, None, s)]
    total_cost = 0
    while Q:
        w, p, u = heappop(Q)
        if u in P: continue
        P[u] = p
        total_cost += w
        for v, w in G[u].items():
            heappush(Q, (w, u, v))
    print(f"Total cost: {total_cost}")
    return P


# todo optimize
def matrix_prim(G, s):
    P, Q = {}, [(0, None, s)]
    total_cost = 0
    while Q:
        w, p, u = heappop(Q)
        if u in P: continue
        P[u] = p
        total_cost += w
        for i in range(len(G[u])):
            if G[u][i] > 0:
                heappush(Q, (G[u][i], u, i))
    print(f"Total cost: {total_cost}")
    return P