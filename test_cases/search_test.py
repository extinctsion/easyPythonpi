# Import the necessary modules and functions from searchalgorithms.py
import sys,os
sys.path.append(f'{os.getcwd()[:-11]}')
from easyPythonpi import *
# Create a sample graph for testing
graph = {
    'A': ['B', 'C'],
    'B': ['C', 'D'],
    'C': ['D'],
    'D': ['C'],
    'E': ['F'],
    'F': ['C'],
}

# Test Breadth-First Search (BFS)
def test_bfs():
    result = bfs(graph, 'A')
    assert result == ['A', 'B', 'C', 'D']

# Test Depth-First Search (DFS)
def test_dfs():
    result = dfs(graph, 'A')
    assert result == ['A', 'C', 'D', 'B']

# Run the tests
test_bfs()
test_dfs()
