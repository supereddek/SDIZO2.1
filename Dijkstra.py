from heapq import heappush, heappop
from BelmanFord import relax, get_cycle


def list_dijkstra(graph, start, dest):
    distances, parents = {start: 0}, {}
    queue, visited = [(0, start)], set()      # Est., tree, queue, visited
    while queue:                                    # Still unprocessed nodes?
        _, u = heappop(queue)                       # Node with lowest estimate
        if u in visited: continue                     # Already visited? Skip it
        visited.add(u)                                # We've visited it now
        for v in graph.edges[u]:                          # Go through all its neighbors
            relax(graph.edges, u, v, distances, parents)                # Relax the out-edge
            heappush(queue, (distances[v], v))              # Add to queue, w/est. as pri
    get_cycle(parents, distances, start, dest)
    return distances, parents                                 # Final D and P returned


def matrix_dijkstra(graph, start, dest):
    distances, parents = {start: 0}, {},
    queue, visited = [(0, start)], set()            # Est., tree, queue, visited
    while queue:                                    # Still unprocessed nodes?
        _, u = heappop(queue)                       # Node with lowest estimate
        if u in visited: continue                     # Already visited? Skip it
        visited.add(u)                                # We've visited it now
        for v in range(graph.vertices):                    # Go through all its neighbors
            if graph.edges[u][v] != 0:
                relax(graph.edges, u, v, distances, parents)          # Relax the out-edge
                heappush(queue, (distances[v], v))              # Add to queue, w/est. as pri
    get_cycle(parents, distances, start, dest)
    return distances, parents                                 # Final D and P returned





