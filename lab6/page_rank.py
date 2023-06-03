import networkx as nx
import random
import numpy as np
from lab4.di_shape_conversion import *

def pagerank_a(graph, d=0.15, max_iter=100):
    # Tworzenie macierzy sąsiedztwa
    # adjacency_matrix = nx.to_numpy_array(graph)
    adjacency_matrix = nx_digraph_object_to_adj_matrix(graph)

    # Obliczanie stopni wierzchołków
    outdegrees = np.sum(adjacency_matrix, axis=0)

    # Normalizacja macierzy sąsiedztwa
    adjacency_matrix = adjacency_matrix / outdegrees

    # Liczba wierzchołków w grafie
    num_nodes = len(graph)

    # Inicjalizacja wektora PageRank
    pagerank_vector = np.ones(num_nodes) / num_nodes

    # Iteracyjne obliczanie PageRank
    for _ in range(max_iter):
        teleportation_vector = np.ones(num_nodes) / num_nodes
        pagerank_vector = (1 - d) * np.matmul(adjacency_matrix, pagerank_vector) + d * teleportation_vector

    return pagerank_vector

def pagerank_b(graph, d=0.15, max_iter=100, tolerance=1e-6):
    num_nodes = graph.number_of_nodes()

    # Tworzenie macierzy sąsiedztwa
    adjacency_matrix = nx.to_numpy_array(graph)

    # Obliczanie stopni wyjściowych wierzchołków
    outdegrees = np.sum(adjacency_matrix, axis=1)

    # Inicjalizacja wektora obsadzeń p0
    p = np.ones(num_nodes) / num_nodes

    # Iteracyjne obliczanie PageRank
    for _ in range(max_iter):
        p_new = (1 - d) * np.matmul(adjacency_matrix.T / outdegrees, p) + d / num_nodes

        # Sprawdzanie warunku zbieżności
        if np.linalg.norm(p - p_new) < tolerance:
            break

        p = p_new

    return p

def print_pagerank(G, pagerank_values):
    for node, pagerank_value in zip(G.nodes(), pagerank_values):
        print(f'{node}: {pagerank_value}')

def generate_random_suitable_digraph(num_nodes):
    # Create an empty directed graph
    digraph = nx.DiGraph()

    # Add nodes to the graph
    for i in range(num_nodes):
        digraph.add_node(i)

    # Add at least one outgoing edge from each node
    for node in digraph.nodes():
        # Get a random target node
        target_node = random.choice(list(set(digraph.nodes()) - set([node])))

        # Add the edge
        digraph.add_edge(node, target_node)

    # Add additional random edges
    for node in digraph.nodes():
        while digraph.out_degree(node) == 1:
            target_node = random.choice(list(set(digraph.nodes()) - set([node])))
            digraph.add_edge(node, target_node)

    return digraph