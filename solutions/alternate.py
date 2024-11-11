from collections import defaultdict, deque

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


# BFS
def bfs(s, t):
    visited = set()
    queue = deque([s])
    while queue:
        node = queue.popleft()
        if node == t:
            return True # found path from s to t
        if node in visited:
            continue
        visited.add(node)
        queue.extend(graph[node])
    return False # no path from s to t

# Result
print(bfs(s, t))