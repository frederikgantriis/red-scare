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
    if u in reds and v in reds:
        continue
    if u not in reds and v not in reds:
        continue
    
    if e == "--": # undirected
        graph[u].append(v)
        graph[v].append(u)
    else: # directed
        graph[u].append(v)

# Result
print(bfs(graph, s, t))
