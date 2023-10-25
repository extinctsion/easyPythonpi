#!/usr/bin/env python
#-*- coding: utf-8 -*-

# Import the necessary modules and functions from searchalgorithms.py

from easyPythonpi.methods.search import *
import unittest

class TestSearch(unittest.TestCase):
    def setUp(self) -> None:
        # Create a sample graph for testing
        self.graph = {
            'A': ['B', 'C'],
            'B': ['C', 'D'],
            'C': ['D'],
            'D': ['C'],
            'E': ['F'],
            'F': ['C'],
        }
        return super().setUp()

    # Test Breadth-First Search (BFS)
    def test_bfs(self):
        result = bfs(self.graph, 'A')
        self.assertEqual(result, ['A', 'B', 'C', 'D'])

    # Test Depth-First Search (DFS)
    def test_dfs(self):
        result = dfs(self.graph, 'A')
        self.assertEqual(result, ['A', 'C', 'D', 'B'])

# Run the tests
if __name__ =="__main__":
    unittest.main()
