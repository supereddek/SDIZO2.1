inf = float('inf')


def relax(W, u, v, D, P):
    d = D.get(u,inf) + W[u][v]                  # Possible shortcut estimate
    if d < D.get(v,inf):                        # Is it really a shortcut?
        D[v], P[v] = d, u                       # Update estimate and parent
        return True                             # There was a change!


def list_bellman_ford(G, s, dest):
    D, P = {s:0}, {}                            # Zero-dist to s; no parents
    for rnd in range(G.vertices - 1):           # n = len(G) rounds
        changed = False                         # No changes in round so far
        for u in range(G.vertices):             # For every from-node...
            for v in G.edges[u]:                      # ... and its to-nodes...
                if relax(G.edges, u, v, D, P):        # Shortcut to v from u?
                    changed = True              # Yes! So something changed
        if not changed: break                   # No change in round: Done
    else:                                       # Not done before round n?
        raise ValueError('negative cycle')      # Negative cycle detected
    get_cycle(P, s, dest)
    return D, P                                 # Otherwise: D and P correct


def matrix_bellman_ford(G, s, dest):
    D, P = {s:0}, {}                            # Zero-dist to s; no parents
    for rnd in range(G.vertices - 1):           # n = len(G) rounds
        changed = False                         # No changes in round so far
        for u in range(G.vertices):             # For every from-node...
            for v in range(G.vertices):                      # ... and its to-nodes...
                if G.edges[u][v] != 0:
                    if relax(G.edges, u, v, D, P):        # Shortcut to v from u?
                        changed = True              # Yes! So something changed
        if not changed: break                   # No change in round: Done
    else:                                       # Not done before round n?
        raise ValueError('negative cycle')      # Negative cycle detected
    get_cycle(P, s, dest)
    return D, P


# reads Parent dictionary to find path to destination
def get_cycle(P, start, dest):
    cycle = []
    new_dest = dest
    while 1:
        cycle.insert(0, new_dest)
        new_dest = P[new_dest]
        if new_dest == start: break
    cycle.insert(0, start)
    print(f"Cycle from {start} to {dest}: {cycle}")