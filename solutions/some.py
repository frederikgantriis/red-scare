from collections import defaultdict
from enum import Enum

from flow import flow
from many import topological_order, longest_path


class Color(Enum):
    WHITE = 0
    GREY = 1
    BLACK = 2


def main():
    n, m, r = map(int, input().split())
    s, t = input().split()

    vertices = []
    reds = defaultdict(lambda: False)
    flow_graph = defaultdict(lambda: defaultdict(int))

    for _ in range(n):
        v = input()
        if v.endswith("*"):
            v = v.split()[0]
            reds[v] = True
        vertices.append(v + "_i")
        vertices.append(v + "_o")

        flow_graph[v + "_i"][v + "_o"] = 1

    many_graph = defaultdict(list)
    reverse_many_graph = defaultdict(list)
    is_directed = True

    # Read graph edges
    for _ in range(m):
        u, line, v = input().split()

        flow_graph[u + "_o"][v + "_i"] = 1
        many_graph[u].append(v)
        reverse_many_graph[v].append(u)

        if line == "--":
            flow_graph[v + "_o"][u + "_i"] = 1
            is_directed = False

    if is_directed:
        colors = defaultdict(lambda: Color.WHITE)
        order = []
        cycle_free = topological_order(many_graph, colors, s, t, order)
        if not cycle_free:
            print("-")
            sys.exit()
        values = longest_path(reverse_many_graph, order, reds)

        if values[s] >= 1:
            print("true")
        else:
            print("false")
    else:
        s_prime = s + "_p"
        t_prime = t + "_p"
        flow_graph[s_prime][s + "_i"] = 1
        flow_graph[s_prime][t + "_i"] = 1

        works = False
        for red in reds.keys():
            flow_graph[red + "_i"][red + "_o"] = 2
            flow_graph[red + "_o"][t_prime] = 2

            fv, fg, cut = flow(flow_graph, s_prime, t_prime)

            flow_graph[red + "_i"][red + "_o"] = 1
            flow_graph[red + "_o"][t_prime] = 0

            if fv >= 2:
                works = True
                break

        if works:
            print("true")
        else:
            print("false")


if __name__ == "__main__":
    main()
