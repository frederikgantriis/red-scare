from collections import defaultdict

from pathfinding import bfs

n, m, r = map(int, input().split())
s, t = input().split()

reds = set()
graph = defaultdict(list)

for _ in range(n):
    v = input().split()
    if len(v) > 1: 
        reds.add(v[0])

for _ in range(m):
    u, e, v = input().split()
    if (u in reds or v in reds) and (u != s or u != t or v != s or v != t):
        continue
    
    if e == "--": # undirected
        graph[u].append(v)
        graph[v].append(u)
    else: # directed
        graph[u].append(v)

print(len(bfs(graph, s, t)) - 1)
