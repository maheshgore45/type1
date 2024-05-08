import heapq

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))  # For undirected graph

    def dijkstra_shortest_paths(self, start):
        distances = [float('inf')] * self.vertices
        distances[start] = 0
        min_heap = [(0, start)]  # (distance, node)
        visited = set()

        while min_heap:
            dist, node = heapq.heappop(min_heap)

            if node in visited:
                continue

            visited.add(node)

            for neighbor, weight in self.graph[node]:
                if neighbor not in visited and dist + weight < distances[neighbor]:
                    distances[neighbor] = dist + weight
                    heapq.heappush(min_heap, (dist + weight, neighbor))

        return distances

# Take user input for the graph
num_vertices = int(input("Enter the number of vertices: "))
num_edges = int(input("Enter the number of edges: "))

g = Graph(num_vertices)

print("Enter edges (start end weight):")
for _ in range(num_edges):
    u, v, w = map(int, input().split())
    g.add_edge(u, v, w)

start_node = int(input("Enter the starting node for shortest paths: "))
distances = g.dijkstra_shortest_paths(start_node)

print("Shortest Distances from Node", start_node, "to all other nodes:")
for i in range(len(distances)):
    print("Node:", i, "Distance:", distances[i])

#Enter the number of vertices: 5
#Enter the number of edges: 7
#Enter edges in the format 'source destination weight':
#0 1 4
#0 2 2
#1 2 5
#1 3 10
#2 3 3
#2 4 2
#3 4 6
#Enter the starting vertex: 0
#Shortest distances from the starting vertex:
#Distance to 0: 0
#Distance to 1: 4
#istance to 2: 2
#Distance to 3: 5
#Distance to 4: 4

#=== Code Execution Successful ===