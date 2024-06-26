class Graph: 
    def __init__(self, vertices): 
        self.V = vertices 
        self.vertices_dict = {}   
        self.graph = [[] for _ in range(vertices)] 
 
    def add_edge(self, u, v, w): 
        u_index = self.get_vertex_index(u) 
        v_index = self.get_vertex_index(v) 
        self.graph[u_index].append((v_index, w)) 
        self.graph[v_index].append((u_index, w)) 
 
    def get_vertex_index(self, vertex): 
        if vertex not in self.vertices_dict: 
            index = len(self.vertices_dict) 
            self.vertices_dict[vertex] = index 
            return index 
        return self.vertices_dict[vertex] 
 
    def prim_mst(self): 
        visited = [False] * self.V 
        key = [float('inf')] * self.V 
        parent = [-1] * self.V 
 
        key[0] = 0 
        parent[0] = -1 
 
        for _ in range(self.V): 
            u = self.min_key(key, visited) 
            visited[u] = True 
 
            for v, weight in self.graph[u]: 
                if not visited[v] and weight < key[v]: 
                    key[v] = weight 
                    parent[v] = u 
 
        mst_edges = [] 
        total_cost = 0 
        for i in range(1, self.V): 
            mst_edges.append((self.get_vertex_name(parent[i]), self.get_vertex_name(i), key[i])) 
            total_cost += key[i] 
        return mst_edges, total_cost 
 
    def min_key(self, key, visited): 
        min_val = float('inf') 
        min_index = -1 
 
        for v in range(self.V): 
            if not visited[v] and key[v] < min_val: 
                min_val = key[v] 
                min_index = v 
 
        return min_index 
 
    def get_vertex_name(self, index): 
        for name, idx in self.vertices_dict.items(): 
            if idx == index: 
                return name 

def take_input(): 
    vertices = int(input("Enter the number of vertices: ")) 
    edges = int(input("Enter the number of edges: ")) 
    g = Graph(vertices) 
    print("Enter edges in the format 'source destination weight': ") 
    for _ in range(edges): 
        u, v, w = input().split() 
        g.add_edge(u, v, int(w))  
    return g 
    
print("Enter graph details:") 
graph = take_input() 
mst_edges, total_cost = graph.prim_mst() 
print("Minimum Spanning Tree edges using Prim's algorithm:") 
for edge in mst_edges: 
    print(edge) 
print("Total cost of Minimum Spanning Tree:", total_cost)