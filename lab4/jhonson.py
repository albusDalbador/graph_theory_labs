import numpy as np
from lab4.bellman_ford import bellman_ford
# from lab3.dijkstra import invoke_dijkstra_alg

def dijkstra(G, node):
    num_nodes = G.number_of_nodes()
    d = np.full(num_nodes, np.inf)
    p = [None] * num_nodes
    d[node] = 0

    achieved = []
    while len(achieved) != num_nodes:
        min_weight = np.min([x for ind, x in enumerate(d) if ind not in achieved])
        u = int([x for x in np.where(d == min_weight)[0] if x not in achieved][0])
        achieved.append(u)

        for v in G.neighbors(u):
            weight = G.get_edge_data(u, v)['weight']
            if d[v] > d[u] + weight:
                d[v] = d[u] + weight
                p[v] = u

    return d, p

def johnson_algorithm(digraph):
    num_nodes = digraph.number_of_nodes()

    # Create a new graph with an additional node
    extended_graph = digraph.copy()
    extended_graph.add_node(num_nodes)

    # Add zero-weight edges from the additional node to all other nodes
    for node in range(num_nodes):
        extended_graph.add_edge(num_nodes, node, weight=0)

    # Run Bellman-Ford algorithm to get distance adjustments
    distance_dict, _ = bellman_ford(extended_graph, num_nodes)

    # Initialize the array for shortest distances
    shortest_distances = np.zeros((num_nodes, num_nodes), dtype=float)

    # Run Dijkstra's algorithm for each node
    for source in range(num_nodes):
        distances, _ = dijkstra(digraph, source)

        for target in range(num_nodes):
            shortest_distances[source][target] = distances[target] - distance_dict[source] + distance_dict[target]

    return shortest_distances