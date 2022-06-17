from heapq import heappush, heappop
from BelmanFord import relax, get_cycle


def list_dijkstra(G, s, dest):
    D, P, Q, S = {s:0}, {}, [(0,s)], set()      # Est., tree, queue, visited
    while Q:                                    # Still unprocessed nodes?
        _, u = heappop(Q)                       # Node with lowest estimate
        if u in S: continue                     # Already visited? Skip it
        S.add(u)                                # We've visited it now
        for v in G.edges[u]:                          # Go through all its neighbors
            relax(G.edges, u, v, D, P)                # Relax the out-edge
            heappush(Q, (D[v], v))              # Add to queue, w/est. as pri
    get_cycle(P, s, dest)
    return D, P                                 # Final D and P returned


def matrix_dijkstra(G, s, dest):
    D, P, Q, S = {s:0}, {}, [(0,s)], set()      # Est., tree, queue, visited
    while Q:                                    # Still unprocessed nodes?
        _, u = heappop(Q)                       # Node with lowest estimate
        if u in S: continue                     # Already visited? Skip it
        S.add(u)                                # We've visited it now
        for v in range(G.vertices):                    # Go through all its neighbors
            if G.edges[u][v] != 0:
                relax(G.edges, u, v, D, P)          # Relax the out-edge
                heappush(Q, (D[v], v))              # Add to queue, w/est. as pri
    get_cycle(P, s, dest)
    return D, P                                 # Final D and P returned