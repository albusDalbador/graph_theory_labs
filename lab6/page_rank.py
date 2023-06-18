import networkx as nx
import random
import numpy as np
from lab4.di_shape_conversion import *

def pagerank_a(graph, d=0.15, max_iter=100):
    # Convert digraph to adjacency matrix
    adjacency_matrix = nx.to_numpy_array(graph)

    # Calculate outdegrees of nodes
    outdegrees = np.sum(adjacency_matrix, axis=0)

    # Normalize adjacency matrix and handle zero outdegrees
    for i, outdegree in enumerate(outdegrees):
        if outdegree > 0:
            adjacency_matrix[:, i] /= outdegree
        else:
            adjacency_matrix[:, i] = 1 / len(graph)

    # Number of nodes in the graph
    num_nodes = len(graph)

    # Initialize PageRank vector
    pagerank_vector = np.ones(num_nodes) / num_nodes

    # Iteratively calculate PageRank
    for _ in range(max_iter):
        teleportation_vector = np.ones(num_nodes) / num_nodes
        pagerank_vector = (1 - d) * np.matmul(adjacency_matrix, pagerank_vector) + d * teleportation_vector

    return pagerank_vector

def pagerank_b(graph, d=0.15, epsilon=1e-8, max_iter=100):
    n = graph.number_of_nodes()
    A = nx.to_numpy_array(graph)
    P = np.zeros((n, n))

    # Tworzenie macierzy stochastycznej P
    for i in range(n):
        di = np.sum(A[i])
        for j in range(n):
            if di > 0:
                P[i, j] = (1 - d) * A[i, j] / di + d / n
            else:
                P[i, j] = 1 / n

    # Inicjalizacja wektora obsadzeń
    p = np.ones(n) / n

    # Iteracyjne obliczenie wektora obsadzeń
    for _ in range(max_iter):
        p_next = np.dot(p, P)
        if np.linalg.norm(p_next - p, 1) < epsilon:
            break
        p = p_next

    # Normalizacja wektora obsadzeń
    p /= np.sum(p)

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