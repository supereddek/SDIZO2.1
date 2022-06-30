inf = float('inf')


def relax(edges, u, v, distances, parents):
    dist = distances.get(u, inf) + edges[u][v]                  # Possible shortcut estimate
    if dist < distances.get(v, inf):                        # Is it really a shortcut?
        distances[v], parents[v] = dist, u                  # Update estimate and parent
        return True                                      # There was a change!


def list_bellman_ford(graph, start, dest):
    distances, parents = {start: 0}, {}                                    # Zero-dist to start; no parents
    for step in range(graph.vertices - 1):                   # n = len(G) rounds
        changed = False                                 # No changes in round so far
        for u in range(graph.vertices):                     # For every from-node...
            for v in graph.edges[u]:                                # ... and its to-nodes...
                if relax(graph.edges, u, v, distances, parents):    # Shortcut to v from u?
                    changed = True                                   # Yes! So something changed
        if not changed: break                           # No change in round: Done
    else:                                               # Not done before round n?
        raise ValueError('negative cycle')              # Negative cycle detected
    get_cycle(parents, distances, start, dest)
    return distances, parents                           # Otherwise: D and parents correct


def matrix_bellman_ford(graph, start, dest):
    distances, parents = {start: 0}, {}                                # Zero-dist to start; no parents
    for step in range(graph.vertices - 1):                   # n = len(G) rounds
        changed = False                                 # No changes in round so far
        for u in range(graph.vertices):                     # For every from-node...
            for v in range(graph.vertices):                 # ... and its to-nodes...
                if graph.edges[u][v] != 0:
                    if relax(graph.edges, u, v, distances, parents):      # Shortcut to v from u?
                        changed = True                  # Yes! So something changed
        if not changed: break                           # No change in round: Done
    else:                                               # Not done before round n?
        raise ValueError('negative cycle')              # Negative cycle detected
    get_cycle(parents, distances, start, dest)
    return distances, parents


# reads Parent dictionary to find path to destination
def get_cycle(parents, distances, start, dest):
    if dest in distances.keys():                                # Check if dest is reachable from start
        cycle = []
        new_dest = dest
        while new_dest != start:
            cycle.insert(0, new_dest)
            new_dest = parents[new_dest]
        cycle.insert(0, start)
        print(f"Cycle from {start} to {dest}: {cycle}")
        print(f"Cycle length is: {distances[dest]}")
    else:
        print(f"Nie ma drogi z {start} do {dest}")



