#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest

from easyPythonpi.methods.graph import Graph
from easyPythonpi.methods.search import *

# Import the necessary modules and classes from graph.py
# from Graph import Graph


# Create an instance of the Graph class


class TestGraph(unittest.TestCase):
    def setUp(self) -> None:
        self.graph = Graph()
        self.graph.add_edge("A", "B")
        self.graph.add_edge("A", "C")
        self.graph.add_edge("B", "C")
        self.graph.add_edge("C", "A")
        assert "A" in self.graph.graph
        assert "B" in self.graph.graph
        assert "C" in self.graph.graph
        assert "B" in self.graph.graph["A"]
        assert "C" in self.graph.graph["A"]
        assert "C" in self.graph.graph["B"]

    def test_bfs(self):
        graph = Graph()
        graph.add_edge("A", "B")
        graph.add_edge("A", "C")
        graph.add_edge("B", "C")
        graph.add_edge("C", "D")
        result = bfs(graph.graph, "A")
        self.assertCountEqual(["A", "B", "C", "D"], result)

    def test_dfs(self):
        graph = Graph()
        graph.add_edge("A", "B")
        graph.add_edge("A", "C")
        graph.add_edge("B", "C")
        graph.add_edge("C", "D")
        result = dfs(graph.graph, "A")
        self.assertCountEqual(["A", "C", "D", "B"], result)
