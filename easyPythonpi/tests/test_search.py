#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest

from easyPythonpi.methods.search import *

# Import the necessary modules and functions from searchalgorithms.py


class Search(unittest.TestCase):
    def test_bfs(self):
        graph = {
            "A": ["B", "C"],
            "B": ["C", "D"],
            "C": ["D"],
            "D": ["C"],
            "E": ["F"],
            "F": ["C"],
        }
        result = bfs(graph, "A")
        self.assertCountEqual(["A", "B", "C", "D"], result)

    def test_dfs(self):
        graph = {
            "A": ["B", "C"],
            "B": ["C", "D"],
            "C": ["D"],
            "D": ["C"],
            "E": ["F"],
            "F": ["C"],
        }
        result = dfs(graph, "A")
        self.assertCountEqual(["A", "C", "D", "B"], result)
