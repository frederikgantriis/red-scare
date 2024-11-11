"""
Path finding utilities
"""

from collections import defaultdict
from queue import PriorityQueue
from math import inf

def bfs(graph, s, t):
    visited = set()
    queue = [[s]]
    while queue:
        path = queue.pop(0)
        v = path[-1]
        visited.add(v)
        for node in graph[v]:
            if node == t:
                return path # found path from s to t
            if node not in visited:
                visited.add(node)
                queue.append(path + [node])
    return [] # no path from s to t


def dijkstra(graph, weight, s, t):
    pq = PriorityQueue()
    pq.put((weight[s], s))
    dist_to = defaultdict(lambda: inf)
    edge_to = defaultdict(lambda: None)
    while not pq.empty():
        dist_to_node, node = pq.get()
        if node == t:
            return dist_to_node
        if dist_to_node > dist_to[node]:
            continue
        for neighbor in graph[node]:
            dist = dist_to_node + weight[neighbor]
            if dist < dist_to[neighbor]:
                dist_to[neighbor] = dist
                edge_to[neighbor] = node
                pq.put((dist, neighbor))
    return -1
