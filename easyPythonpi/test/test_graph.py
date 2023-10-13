#!/usr/bin/env python
#-*- coding: utf-8 -*-

# Import the necessary modules and classes from graph.py
#from Graph import Graph

from easyPythonpi.methods.graph import Graph
from easyPythonpi.methods.search import *
import unittest

# Create an instance of the Graph class
class TestGraph(unittest.TestCase):
    def setUp(self) -> None:
        self.graph = Graph()
        self.graph.add_edge('A', 'B')
        self.graph.add_edge('A', 'C')
        self.graph.add_edge('B', 'C')
        self.graph.add_edge('C', 'D')
        self.v1 = 'test'
        self.v2 = 'result'
        return super().setUp()
    
    def test_is_edge_exist(self):
        self.assertTrue(self.graph.is_edge_exist('A', 'B'))
        self.assertFalse(self.graph.is_edge_exist('A', 'D'))

    def test_is_vertex_exist(self):
        self.assertTrue(self.graph.is_vertex_exist('A'))
        self.assertFalse(self.graph.is_vertex_exist('Z'))

    def test_add_edge(self):
        self.graph.add_edge(self.v1, self.v2)
        self.assertTrue(self.graph.is_edge_exist(self.v1, self.v2), 'edge not added')
        self.graph.remove_edge(self.v1, self.v2)
    
    def test_remove_edge(self):
        self.graph.add_edge(self.v1, self.v2)
        self.graph.remove_edge(self.v1, self.v2)
        self.assertFalse(self.graph.is_edge_exist(self.v1, self.v2), 'edge not removed')

    def test_add_vertex(self):
        self.graph.add_vertex(self.v1)
        self.assertTrue(self.graph.is_vertex_exist(self.v1),'vertex not added')
        self.graph.remove_vertex(self.v1)

    def test_remove_vertex(self):
        self.graph.add_vertex(self.v1)
        self.graph.remove_vertex(self.v1)
        self.assertFalse(self.graph.is_vertex_exist(self.v1),'vertex not removed')

    def test_clear(self):
        graph = Graph()
        graph.add_edge(self.v1, self.v2)
        self.assertNotEqual(len(graph.get_vertices()), 0)
        graph.clear()
        self.assertEqual(len(graph.get_vertices()), 0)


# Run the test
if __name__ == "__main__":
    unittest.main()
