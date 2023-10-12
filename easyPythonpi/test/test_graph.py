#!/usr/bin/env python
#-*- coding: utf-8 -*-

# Import the necessary modules and classes from graph.py
#from Graph import Graph

from easyPythonpi.methods.graph import Graph
from easyPythonpi.methods.search import *

# Create an instance of the Graph class

graph = Graph()

# Test adding edges
def test_add_edge():
    graph.add_edge('A', 'B')
    graph.add_edge('A', 'C')
    graph.add_edge('B', 'C')
    graph.add_edge('C', 'A')
    assert 'A' in graph.graph
    assert 'B' in graph.graph
    assert 'C' in graph.graph
    assert 'B' in graph.graph['A']
    assert 'C' in graph.graph['A']
    assert 'C' in graph.graph['B']


def test_bfs():
    graph2=Graph()
    graph2.add_edge('A', 'B')
    graph2.add_edge('A', 'C')
    graph2.add_edge('B', 'C')
    graph2.add_edge('C', 'D')
    result = bfs(graph2.graph, 'A')
    assert result == ['A', 'B', 'C', 'D']

# Test Depth-First Search (DFS) from main.py
def test_dfs():
    graph3=Graph()
    graph3.add_edge('A', 'B')
    graph3.add_edge('A', 'C')
    graph3.add_edge('B', 'C')
    graph3.add_edge('C', 'D')
    result = dfs(graph3.graph, 'A')
    assert result == ['A', 'C', 'D', 'B']

# Run the test
test_bfs()
test_dfs()
test_add_edge()
