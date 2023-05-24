import numpy as np
import networkx as nx
from lab4.di_shape_conversion import *

def read_digraph_from_inc_matrix(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    incidence_matrix = []
    for line in lines:
        row = list(map(int, line.strip().split()))
        incidence_matrix.append(row)

    incidence_matrix = np.array(incidence_matrix)
    digraph = inc_matrix_to_nx_digraph_object(incidence_matrix)
    return digraph

def read_digraph_from_adj_matrix(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    adjacency_matrix = []
    for line in lines:
        row = list(map(int, line.strip().split()))
        adjacency_matrix.append(row)

    adjacency_matrix = np.array(adjacency_matrix)
    digraph = adj_matrix_to_nx_digraph_object(adjacency_matrix)
    return digraph

def read_digraph_from_adjacency_list(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    adjacency_list = {}
    for line in lines:
        data = line.strip().split()
        node = int(data[0])
        neighbors = list(map(int, data[1:]))
        adjacency_list[node] = neighbors

    digraph = adj_list_to_nx_digraph_object(adjacency_list)
    return digraph