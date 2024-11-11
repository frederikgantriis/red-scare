"""
Path finding utilities
"""

from collections import defaultdict
from queue import PriorityQueue
from math import inf

def bfs(graph, s, t):
    visited = set()
    queue = [s]
    while queue:
        node = queue.pop(0)
        if node == t:
            return True # found path from s to t
        if node in visited:
            continue
        visited.add(node)
        queue.extend(graph[node])
    return False # no path from s to t


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
