import networkx as nx
import random
import matplotlib.pyplot as plt

def generate_random_digraph(n, p):
    digraph = nx.DiGraph()
    digraph.add_nodes_from(range(n))

    for source in range(n):
        for destination in range(n):
            if source != destination and random.random() < p:
                digraph.add_edge(source, destination)

    return digraph

def visualize_digraph_with_weights(digraph):
    pos = nx.spring_layout(digraph)
    edge_labels = nx.get_edge_attributes(digraph, "weight")

    nx.draw(digraph, pos, with_labels=True)
    nx.draw_networkx_edge_labels(digraph, pos, edge_labels=edge_labels)

    plt.show()