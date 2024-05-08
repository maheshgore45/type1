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

# print("Minimal Spanning Tree (MST):")
# for node, cost in mst:
#     print(f"Edge: {start_node} - {node}, Cost: {cost}")

# print("Total Cost of MST:", total_cost)

print("Minimal Spanning Trees (MST):")
for mst, cost in mst:
    print("Tree:")
    for parent, node, cost in mst:
        print(f"Edge: {parent} - {node}, Cost: {cost}")
    print("Total Cost of Tree:", cost)
    print()

print("Total Cost of MST:", total_cost)





#option 2

# import heapq

# graph = {
#         'A': [(3, 'D', 'A'), (3, 'C', 'A'), (2, 'B', 'A')],
#         'B': [(2, 'A', 'B'), (4, 'C', 'B'), (3, 'E', 'B')],
#         'C': [(3, 'A', 'C'), (5, 'D', 'C'), (6, 'F', 'C'), (1, 'E', 'C'), (4, 'B', 'C')],
#         'D': [(3, 'A', 'D'), (5, 'C', 'D'), (7, 'F', 'D')],
#         'E': [(8, 'F', 'E'), (1, 'C', 'E'), (3, 'B', 'E')],
#         'F': [(9, 'G', 'F'), (8, 'E', 'F'), (6, 'C', 'F'), (7, 'D', 'F')],
#         'G': [(9, 'F', 'G')],
#     }

# def prims(graph, start='A'):
#     unvisited = list(graph.keys())
#     visited = []
#     total_cost = 0
#     MST = []

#     unvisited.remove(start)
#     visited.append(start)

#     heap = graph[start]
#     heapq.heapify(heap)

#     while unvisited:
#         (cost, n1, n2) = heapq.heappop(heap)
#         new_node = None

#         if n1 in unvisited and n2 in visited:
#             new_node = n1
#             MST.append((cost, n2, n1))
#         elif n2 in unvisited and n1 in visited:
#             new_node = n2
#             MST.append((cost, n1, n2))

#         if new_node != None:
#             unvisited.remove(new_node)
#             visited.append(new_node)
#             total_cost += cost

#             for node in graph[new_node]:
#                 heapq.heappush(heap, node)

#     return MST, total_cost

# def main():
#     MST, total_cost = prims(graph, 'A')
#     print(f'Minimum spanning tree: {MST}')
#     print(f'Total cost: {total_cost}')

# main()