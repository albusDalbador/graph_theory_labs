import networkx as nx
from shape_conversion import *


def draw_from_adj_matrix(adj_matrix):
    g = nx.Graph(directed=False)
    num_of_nodes = adj_matrix.shape[0]

    for ind in range(num_of_nodes):
        g.add_node(ind)
    
    for i in range(num_of_nodes):
        for j in range(i+1,num_of_nodes):
            if adj_matrix[i,j] == 1:
                g.add_edge(i,j)

    nx.draw_circular(g,with_labels=True)


def draw_from_adj_list(adj_list):
    adj_matrix = adj_list_to_adj_matrix(adj_list)
    draw_from_adj_matrix(adj_matrix)


def draw_from_inc_matrix(inc_matrix):
    adj_matrix = inc_matrix_to_adj_matrix(inc_matrix)
    draw_from_adj_matrix(adj_matrix)
    

