from heapq import heappop, heappush


def list_prim(graph, start=0):
    edges, queue = {}, [(0, None, start)]               # Start from empty tree, put start v in stack
    total_cost = 0
    while queue:
        weight, parent, u = heappop(queue)              # Take the lightest edge from stack
        if u in edges: continue                         # If already in tree, skip
        edges[u] = parent                               # Else add to tree
        total_cost += weight
        for v, weight in graph.edges[u].items():        # Get neighbours on stack
            heappush(queue, (weight, u, v))
    print(f"Total cost: {total_cost}")
    return edges


def matrix_prim(graph, s=0):
    edges, queue = {}, [(0, None, s)]                           # Start from empty tree, put start v in stack
    total_cost = 0
    while queue:
        weight, p, u = heappop(queue)                           # Take the lightest edge from stack
        if u in edges: continue                                 # If already in tree, skip
        edges[u] = p                                            # Else add to tree
        total_cost += weight
        for i in range(len(graph.edges[u])):
            if graph.edges[u][i] > 0:
                heappush(queue, (graph.edges[u][i], u, i))      # Get neighbours on stack
    print(f"Total cost: {total_cost}")
    return edges

