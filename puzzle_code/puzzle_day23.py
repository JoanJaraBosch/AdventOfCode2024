

def part1():
    graph = {}
    with open("../input/day23.txt", "r") as file:
        list_of_connections = []
        for line in file:
            splitted = line.strip().split("-")
            list_of_connections.append(splitted)

        for connect in list_of_connections:
            if connect[0] not in graph:
                graph[connect[0]] = set()
            if connect[1] not in graph:
                graph[connect[1]] = set()
            graph[connect[0]].add(connect[1])
            graph[connect[1]].add(connect[0])
    return graph


def resolve_part1():
    graph = part1()
    # print(graph)
    already_in_set = set()
    for key, connections in graph.items():
        if not key.startswith("t"):
            continue
        for connect_2 in connections:
            for connect_3 in graph[connect_2]:
                if connect_3 in graph[key] and connect_3 != key and tuple(sorted([key, connect_2, connect_3])) not in already_in_set:
                    already_in_set.add(tuple(sorted([key, connect_2, connect_3])))

    # for item in sorted(already_in_set):
    #     print(item)
    return len(already_in_set)


def bron_kerbosch(R, P, X, graph, largest_clique):
    if not P and not X:
        if len(R) > len(largest_clique[0]):
            largest_clique[0] = R
        return

    for vertex in list(P):
        bron_kerbosch(
            R | {vertex},
            P & graph[vertex],
            X & graph[vertex],
            graph,
            largest_clique
        )
        P.remove(vertex)
        X.add(vertex)


def resolve_part2():
    graph = part1()
    R = set()
    P = set(graph.keys())
    X = set()
    largest_clique = [set()]

    # Виклик алгоритму
    bron_kerbosch(R, P, X, graph, largest_clique)

    return ",".join(sorted(largest_clique[0]))
