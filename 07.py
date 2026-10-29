import heapq

class ShortestPath:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = []
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, u, v, w):
        self.edges.append((u, v, w))
        self.graph[u].append((v, w))

    def dijkstra(self, src):
        dist = [float('inf')] * self.vertices
        dist[src] = 0
        heap = [(0, src)]

        while heap:
            d, u = heapq.heappop(heap)

            if d > dist[u]:
                continue

            for v, w in self.graph[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heapq.heappush(heap, (dist[v], v))

        return dist

    def bellman_ford(self, src):
        dist = [float('inf')] * self.vertices
        dist[src] = 0

        for _ in range(self.vertices - 1):
            updated = False

            for u, v, w in self.edges:
                if dist[u] != float('inf') and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    updated = True

            if not updated:
                break

        for u, v, w in self.edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                return "Error: Negative weight cycle detected"

        return dist


sp = ShortestPath(5)

sp.add_edge(0, 1, 4)
sp.add_edge(0, 2, 1)
sp.add_edge(2, 1, 2)
sp.add_edge(1, 3, 1)
sp.add_edge(2, 3, 5)
sp.add_edge(3, 4, 3)

print("Dijkstra:", sp.dijkstra(0))
print("Bellman-Ford:", sp.bellman_ford(0))
