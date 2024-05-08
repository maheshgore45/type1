from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))

    def prim_mst(self, start_node):
        visited = {start_node}
        mst = []
        total_cost = 0
        edges = sorted([(w, u, v) for u in self.graph for v, w in self.graph[u]])

        while len(mst) < len(self.graph) - 1:
            min_edge = None
            min_cost = float('inf')
            for w, u, v in edges:
                if (u in visited) != (v in visited) and w < min_cost:
                    min_edge = (u, v, w)
                    min_cost = w
            
            if min_edge:
                u, v, w = min_edge
                mst.append((u, v, w))
                total_cost += w
                visited.add(v) if v not in visited else visited.add(u)
        
        return mst, total_cost

# Take user input for the graph
g = Graph()
num_edges = int(input("Enter the number of edges: "))

for _ in range(num_edges):
    u, v, w = map(int, input("Enter edge (start end weight): ").split())
    g.add_edge(u, v, w)

start_node = int(input("Enter the starting node for MST: "))
mst, mst_cost = g.prim_mst(start_node)

print("Minimum Spanning Tree (MST):")
for u, v, w in mst:
    print(f"{u} - {v}: {w}")
print("Total Cost of MST:", mst_cost)

