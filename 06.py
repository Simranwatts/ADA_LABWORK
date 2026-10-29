import heapq

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = []

    def add_edge(self, u, v, w):
        self.edges.append((w, u, v))

    def kruskal_mst(self):
        parent = list(range(self.vertices))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        mst = []

        for w, u, v in sorted(self.edges):
            a = find(u)
            b = find(v)

            if a != b:
                mst.append((u, v, w))
                parent[a] = b

            if len(mst) == self.vertices - 1:
                break

        return mst

    def prim_mst(self):
        if self.vertices == 0:
            return []

        adj = [[] for _ in range(self.vertices)]

        for w, u, v in self.edges:
            adj[u].append((w, v))
            adj[v].append((w, u))

        visited = set()
        heap = [(0, 0, -1)]
        mst = []

        while heap and len(visited) < self.vertices:
            w, u, parent = heapq.heappop(heap)

            if u in visited:
                continue

            visited.add(u)

            if parent != -1:
                mst.append((parent, u, w))

            for weight, v in adj[u]:
                if v not in visited:
                    heapq.heappush(heap, (weight, v, u))

        return mst


g = Graph(4)

g.add_edge(0, 1, 10)
g.add_edge(0, 2, 6)
g.add_edge(0, 3, 5)
g.add_edge(1, 3, 15)
g.add_edge(2, 3, 4)

print("Kruskal MST:", g.kruskal_mst())
print("Prim MST:", g.prim_mst())
