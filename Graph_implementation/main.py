from Graph_implementation.Graph import Graph
from Graph_implementation.SearchAlgorithms import bfs, dfs, dijkstra, a_star 

# Create a graph and add edges
g = Graph()
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('B', 'E')
g.add_edge('C', 'F')

# Test BFS and DFS
print("BFS:", bfs(g.graph, 'A'))
print("DFS:", dfs(g.graph, 'A'))
