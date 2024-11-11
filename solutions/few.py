from collections import defaultdict

from pathfinding import dijkstra


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
