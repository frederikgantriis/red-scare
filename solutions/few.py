from collections import defaultdict
from queue import PriorityQueue
from math import inf


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


def main():
    n, m, r = map(int, input().split())
    s, t = input().split()

    vertices = []
    reds = defaultdict(lambda: False)
    weight = defaultdict(lambda: 0)

    for _ in range(n):
        v = input()
        if v.endswith("*"):
            v = v.split()[0]
            reds[v] = True
            weight[v] = 1
        vertices.append(v)

    graph = defaultdict(list)

    # Read graph edges
    for _ in range(m):
        u, line, v = input().split()

        graph[u].append(v)

        if line == "--":
            graph[v].append(u)
    print("Graph read")

    print(dijkstra(graph, weight, s, t))


if __name__ == "__main__":
    main()
