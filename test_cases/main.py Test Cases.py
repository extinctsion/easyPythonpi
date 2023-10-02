# Import the necessary modules and classes from main.py
from easyPythonpi.Graph_implementation.main import Graph, bfs, dfs

# Create an instance of the Graph class
graph = Graph()

# Add edges to the graph
graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('B', 'C')
graph.add_edge('C', 'D')

# Test Breadth-First Search (BFS) from main.py
def test_bfs():
    result = bfs(graph.graph, 'A')
    assert result == ['A', 'B', 'C', 'D']

# Test Depth-First Search (DFS) from main.py
def test_dfs():
    result = dfs(graph.graph, 'A')
    assert result == ['A', 'B', 'C', 'D']

# Run the tests
test_bfs()
test_dfs()
