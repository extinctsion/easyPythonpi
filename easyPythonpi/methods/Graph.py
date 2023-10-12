#!/usr/bin/env python
#-*- coding: utf-8 -*-


class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def get_vertices(self):
        return list(self.graph.keys())

    def get_edges(self):
        edges = []
        for vertex, neighbors in self.graph.items():
            for neighbor in neighbors:
                edges.append((vertex, neighbor))
        return edges

    def is_vertex_exist(self, vertex):
        return vertex in self.graph

    def is_edge_exist(self, u, v):
        return u in self.graph and v in self.graph[u]

    def remove_edge(self, u, v):
        if self.is_edge_exist(u, v):
            self.graph[u].remove(v)

    def remove_vertex(self, vertex):
        if self.is_vertex_exist(vertex):
            del self.graph[vertex]
            for u in self.graph:
                self.graph[u] = [v for v in self.graph[u] if v != vertex]

    def clear(self):
        self.graph = {}

    def __str__(self):
        return str(self.graph)
