import heapq
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v, weight):
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))

    def prim_mst(self, start_node):
        visited = set()
        mst = []
        total_cost = 0
        min_heap = [(0, start_node)]

        while min_heap:
            cost, node = heapq.heappop(min_heap)
            if node not in visited:
                visited.add(node)
                total_cost += cost
                if len(mst) > 0:
                    mst.append((node, cost))
                for neighbor, weight in self.graph[node]:
                    if neighbor not in visited:
                        heapq.heappush(min_heap, (weight, neighbor))

        return mst, total_cost

# Take user input for the graph
g = Graph()
num_edges = int(input("Enter the number of edges: "))

for _ in range(num_edges):
    u, v, weight = map(int, input("Enter edge (start end weight): ").split())
    g.add_edge(u, v, weight)

start_node = int(input("Enter the starting node for MST: "))
mst, total_cost = g.prim_mst(start_node)

print("Minimal Spanning Tree (MST):")
for node, cost in mst:
    print(f"Edge: {start_node} - {node}, Cost: {cost}")

print("Total Cost of MST:", total_cost)

