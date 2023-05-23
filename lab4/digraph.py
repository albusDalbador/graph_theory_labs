import networkx as nx
import random

def generate_digraph(n, p):
    digraph = nx.DiGraph()
    digraph.add_nodes_from(range(n))

    for source in range(n):
        for destination in range(n):
            if source != destination and random.random() < p:
                digraph.add_edge(source, destination)

    return digraph