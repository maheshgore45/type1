class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append((u, v, w))

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, u, v):
        root_u = self.find(parent, u)
        root_v = self.find(parent, v)

        if rank[root_u] < rank[root_v]:
            parent[root_u] = root_v
        elif rank[root_u] > rank[root_v]:
            parent[root_v] = root_u
        else:
            parent[root_v] = root_u
            rank[root_u] += 1

    def kruskal_mst(self):
        result = []
        self.graph.sort(key=lambda x: x[2])
        parent = [i for i in range(self.vertices)]
        rank = [0] * self.vertices
        total_cost = 0

        for u, v, w in self.graph:
            root_u = self.find(parent, u)
            root_v = self.find(parent, v)

            if root_u != root_v:
                result.append((u, v, w))
                total_cost += w
                self.union(parent, rank, root_u, root_v)

        return result, total_cost

# Take user input for the graph
num_vertices = int(input("Enter the number of vertices: "))
num_edges = int(input("Enter the number of edges: "))

g = Graph(num_vertices)

print("Enter edges (start end weight):")
for _ in range(num_edges):
    u, v, w = map(int, input().split())
    g.add_edge(u, v, w)

mst, total_cost = g.kruskal_mst()

print("Minimal Spanning Tree (MST):")
for u, v, w in mst:
    print(f"Edge: {u} - {v}, Cost: {w}")

print("Total Cost of MST:", total_cost)




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
