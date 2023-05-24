import numpy as np
import networkx as nx

def nx_digraph_object_to_inc_matrix(digraph):
    num_nodes = digraph.number_of_nodes()
    num_edges = digraph.number_of_edges()
    incidence_matrix = np.zeros((num_nodes, num_edges))

    node_to_index = {node: index for index, node in enumerate(digraph.nodes())}
    for index, (source, target) in enumerate(digraph.edges()):
        source_index = node_to_index[source]
        target_index = node_to_index[target]
        incidence_matrix[source_index][index] = 1
        incidence_matrix[target_index][index] = -1

    return incidence_matrix

def nx_digraph_object_to_adj_matrix(digraph):
    num_nodes = digraph.number_of_nodes()
    adjacency_matrix = np.zeros((num_nodes, num_nodes))

    for source, target in digraph.edges():
        source_index = source
        target_index = target
        adjacency_matrix[source_index][target_index] = 1

    return adjacency_matrix

def nx_digraph_object_to_adj_list(digraph):
    adjacency_list = {}
    for node in digraph.nodes():
        neighbors = list(digraph.neighbors(node))
        adjacency_list[node] = neighbors

    return adjacency_list

def inc_matrix_to_nx_digraph_object(incidence_matrix):
    num_nodes, num_edges = incidence_matrix.shape
    digraph = nx.DiGraph()

    for edge_index in range(num_edges):
        source_indices = np.where(incidence_matrix[:, edge_index] == 1)[0]
        target_indices = np.where(incidence_matrix[:, edge_index] == -1)[0]

        if len(source_indices) == 1 and len(target_indices) == 1:
            source = source_indices[0]
            target = target_indices[0]
            digraph.add_edge(source, target)

    return digraph

def adj_matrix_to_nx_digraph_object(adjacency_matrix):
    num_nodes = adjacency_matrix.shape[0]
    digraph = nx.DiGraph()

    for source in range(num_nodes):
        for target in range(num_nodes):
            if adjacency_matrix[source, target] == 1:
                digraph.add_edge(source, target)

    return digraph

def adj_list_to_nx_digraph_object(adjacency_list):
    digraph = nx.DiGraph()

    for node, neighbors in adjacency_list.items():
        for neighbor in neighbors:
            digraph.add_edge(node, neighbor)

    return digraph