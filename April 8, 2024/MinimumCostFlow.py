# Author - Shamura Ahmad

class Edge:
    def __init__(self, capacity, cost):
        self.capacity = capacity
        self.cost = cost
        self.flow = 0

# To find single node shortest path

def bellman_ford(graph, source, sink):
    n = len(graph)
    dist = [float('inf')] * n
    dist[source] = 0

    for _ in range(n - 1):
        for u in range(n):
            for v, edge in enumerate(graph[u]):
                if edge.capacity > edge.flow:
                    dist[v] = min(dist[v], dist[u] + edge.cost)

    return dist[sink]

# To find single node shortest path

def dijkstra(graph, source, sink, dist):
    n = len(graph)
    prev = [-1] * n
    visited = [False] * n
    dist[source] = 0

    while True:
        u = -1
        min_dist = float('inf')
        for i in range(n):
            if not visited[i] and dist[i] < min_dist:
                u = i
                min_dist = dist[i]
        if u == -1 or u == sink:
            break
        visited[u] = True
        for v, edge in enumerate(graph[u]):
            if edge.capacity > edge.flow:
                if dist[v] > dist[u] + edge.cost:
                    dist[v] = dist[u] + edge.cost
                    prev[v] = u

    return dist[sink], prev


def min_cost_max_flow(graph, source, sink):
    n = len(graph)
    cost = 0
    while True:
        min_cost = bellman_ford(graph, source, sink)
        if min_cost == float('inf'):
            break

        flow, prev = dijkstra(graph, source, sink, [float('inf')] * n)
        if flow == float('inf'):
            break

        min_caps = float('inf')
        v = sink
        while v != source:
            u = prev[v]
            edge = graph[u][v]
            min_caps = min(min_caps, edge.capacity - edge.flow)
            v = u

        v = sink
        while v != source:
            u = prev[v]
            edge = graph[u][v]
            edge.flow += min_caps
            graph[v][u].flow -= min_caps
            cost += edge.cost * min_caps
            v = u

    return cost


if __name__ == "__main__":
    
    graph = [
        [Edge(0, 0), Edge(10, 1), Edge(5, 2), Edge(0, 0)],      # Dhaka
        [Edge(0, 0), Edge(0, 0), Edge(15, 3), Edge(9, 2)],      # Cumilla
        [Edge(0, 0), Edge(0, 0), Edge(0, 0), Edge(10, 1), Edge(15, 4)],  # Chandpur
        [Edge(0, 0), Edge(0, 0), Edge(0, 0), Edge(0, 0), Edge(10, 1)],   # Sylhet
        [Edge(0, 0), Edge(0, 0), Edge(0, 0), Edge(0, 0), Edge(0, 0)]     # Khulna
    ]

    min_cost = min_cost_max_flow(graph, 0, 4)

    print("Minimum Cost:", min_cost)
