import networkx as nx
import random
import numpy as np
from lab4.digraph import generate_digraph

def generate_random_strong_digraph(n, p):
    while True:
        digraph = generate_digraph(n, p)
        if nx.is_strongly_connected(digraph):
            return digraph

def generate_random_digraph(num_nodes, p, low=-5, high=10):
    digraph = generate_random_strong_digraph(num_nodes, p)
    for u, v in digraph.edges:
        digraph[u][v]["weight"] = random.randint(low, high)
    return digraph


def bellman_ford(digraph, source):
    distance = {node: float("inf") for node in digraph.nodes}
    distance[source] = 0

    for _ in range(len(digraph.nodes) - 1):
        for u, v in digraph.edges:
            weight = digraph[u][v]["weight"]
            if distance[u] + weight < distance[v]:
                distance[v] = distance[u] + weight

    return distance