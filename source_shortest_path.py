import heapq

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, w):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append((v, w))

    def dijkstra_shortest_path(self, start):
        distances = {node: float('inf') for node in self.graph}
        distances[start] = 0
        min_heap = [(0, start)]
        
        while min_heap:
            current_distance, current_node = heapq.heappop(min_heap)
            if current_distance > distances[current_node]:
                continue
            for neighbor, weight in self.graph[current_node]:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(min_heap, (distance, neighbor))
        
        return distances

# Take user input for the graph
g = Graph()
num_edges = int(input("Enter the number of edges: "))

for _ in range(num_edges):
    u, v, w = map(int, input("Enter edge (start end weight): ").split())
    g.add_edge(u, v, w)

start_node = int(input("Enter the starting node: "))
shortest_distances = g.dijkstra_shortest_path(start_node)

print("Shortest distances from node", start_node)
for node, distance in shortest_distances.items():
    print("Node:", node, "-> Shortest Distance:", distance)

