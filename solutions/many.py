import sys
from collections import defaultdict
from enum import Enum

class Color(Enum):
    WHITE = 0
    GREY = 1
    BLACK = 2

def topological_order(graph, colors, current, target, res):
    if colors[current] == Color.GREY:
        return False
    elif colors[current] == Color.BLACK:
        return True
    elif current == target:
        colors[current] = Color.BLACK
        res.append(target)
        return True
    else:
        cycle_free = True
        colors[current] = Color.GREY
        for neighbor in graph[current]:
            cycle_free = cycle_free and topological_order(graph, colors, neighbor, target, res)
        colors[current] = Color.BLACK
        res.append(current)
        return cycle_free

def longest_path(graph, topological_order, reds):
    value_of = defaultdict(lambda: 0)
    for current in topological_order:
        for neighbor in graph[current]:
            value_of[neighbor] = max(value_of[neighbor], value_of[current] + (1 if reds[current] else 0))
    return value_of

def main():
    n, m, r = map(int, input().split())
    s, t = input().split()

    vertices = []

    vertices = []
    reds = defaultdict(lambda: False)

    for _ in range(n):
        v = input()
        if v.endswith("*"):
            v = v.split()[0]
            reds[v] = True
        vertices.append(v)

    graph = defaultdict(list)
    reverse_graph = defaultdict(list)
    is_undirected = False

    # Read graph edges
    for _ in range(m):
        u, line, v = input().split()

        graph[u].append(v)
        reverse_graph[v].append(u)

        if line == "--":
            is_undirected = True
            break

    if is_undirected:
        print("-")
        sys.exit()

    colors = defaultdict(lambda: Color.WHITE)
    order = []
    cycle_free = topological_order(graph, colors, s, t, order)

    if not cycle_free:
        print("-")
        sys.exit()

    values = longest_path(reverse_graph, order, reds)

    print(values[s])

if __name__ == "__main__":
    main()
