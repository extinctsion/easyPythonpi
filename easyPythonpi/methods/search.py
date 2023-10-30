#!/usr/bin/env python
#-*- coding: utf-8 -*-
import sys,os
sys.path.append(f'{os.getcwd()[:-4]}')
import heapq

from collections import deque

visited = []
queue = []   
resultbfs=[]
resultdfs=[]
visitedbfs=[]
visiteddfs=[]
def bfs(graph, node):
  visitedbfs.append(node)
  queue.append(node)

  while queue:
    s = queue.pop(0) 
    if(s!=''):
      resultbfs.append(s)
    if graph[s]!=['']:
     for neighbour in graph[s]:
       if neighbour not in visitedbfs:
         visitedbfs.append(neighbour)
         queue.append(neighbour)
  return resultbfs      

    

def dfs(graph, node):
    if node not in visiteddfs:
         if(node!=''):
            resultdfs.append(node)
         visiteddfs.append(node)
         if(graph[node]!=['']):
          for n in graph[node]:
           dfs(graph, n)
            
   
    return resultdfs


def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        
        if current_distance > distances[current_vertex]:
            continue
        
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances



def a_star(graph, start, goal):
    open_set = [(0, start)]
    came_from = {}
    g_score = {vertex: float('infinity') for vertex in graph}
    g_score[start] = 0
    f_score = {vertex: float('infinity') for vertex in graph}
    f_score[start] = heuristic(start, goal)
    
    while open_set:
        _, current = heapq.heappop(open_set)
        
        if current == goal:
            return reconstruct_path(came_from, current)
        
        for neighbor, cost in graph[current].items():
            tentative_g_score = g_score[current] + cost
            
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score[neighbor], neighbor))
    
    return None

def heuristic(node, goal):
    # Define your heuristic function here (e.g., Manhattan distance, Euclidean distance, etc.)
    pass

def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    return path[::-1]

