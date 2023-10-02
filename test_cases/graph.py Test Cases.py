# Import the necessary modules and classes from graph.py
from easyPythonpi.Graph_implementation.Graph import Graph

# Create an instance of the Graph class
graph = Graph()

# Test adding edges
def test_add_edge():
    graph.add_edge('A', 'B')
    graph.add_edge('A', 'C')
    graph.add_edge('B', 'C')
    assert 'A' in graph.graph
    assert 'B' in graph.graph
    assert 'C' in graph.graph
    assert 'B' in graph.graph['A']
    assert 'C' in graph.graph['A']
    assert 'C' in graph.graph['B']

# Run the test
test_add_edge()
