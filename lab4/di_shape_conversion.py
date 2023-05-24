import numpy as np
import networkx as nx

def nx_digraph_object_to_inc_matrix(digraph):
    num_nodes = digraph.number_of_nodes()
    num_edges = digraph.number_of_edges()
    incidence_matrix = np.zeros((num_nodes, num_edges), dtype=int)
    edge_index = 0
    node_to_index = {node: index for index, node in enumerate(digraph.nodes())}

    for source, target in digraph.edges():
        incidence_matrix[node_to_index[source], edge_index] = 1
        incidence_matrix[node_to_index[target], edge_index] = -1
        edge_index += 1

    return incidence_matrix

def nx_digraph_object_to_adj_matrix(digraph):
    adjacency_matrix = nx.adjacency_matrix(digraph).toarray()
    return adjacency_matrix

def nx_digraph_object_to_adj_list(digraph):
    adjacency_list = {node: list(digraph.neighbors(node)) for node in digraph.nodes()}
    return adjacency_list

def inc_matrix_to_nx_digraph_object(incidence_matrix):
    num_nodes, num_edges = incidence_matrix.shape
    digraph = nx.DiGraph()

    for edge_index in range(num_edges):
        source_nodes = np.where(incidence_matrix[:, edge_index] == 1)[0]
        target_nodes = np.where(incidence_matrix[:, edge_index] == -1)[0]

        for source in source_nodes:
            for target in target_nodes:
                if source != target:  # Exclude self-loops
                    digraph.add_edge(source, target)

    return digraph

def adj_matrix_to_nx_digraph_object(adjacency_matrix):
    digraph = nx.DiGraph(adjacency_matrix)
    return digraph

def adj_list_to_nx_digraph_object(adjacency_list):
    digraph = nx.DiGraph(adjacency_list)
    return digraph