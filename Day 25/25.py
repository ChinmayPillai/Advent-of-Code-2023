day = 25
file_path = "Day " + str(day) + "/" + str(day) + ".txt"
test_path = "Day " + str(day) + "/test.txt"

import networkx as nx

for path in [test_path, file_path]:

    ans = 0
    with open(path, 'r') as file:
        lines = [line.strip() for line in file.read().split('\n')]

    connections = {}

    for line in lines:
        src, dest = line.split(': ')
        dest = dest.split(' ')
        connections[src] = dest

    graph = nx.Graph()
    for c, cc in connections.items():
        for ci in cc:
            graph.add_edge(c, ci)
    cuts = nx.minimum_edge_cut(graph)
    graph.remove_edges_from(cuts)

    a, b = nx.connected_components(graph)
    print(len(a) * len(b))

    print("="*80)
