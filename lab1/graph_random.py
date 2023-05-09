from random import random
import numpy as np
import random

from .shape_conversion import *


def rand_graph_edge_num(num_of_nodes,num_of_edges):
    if (num_of_edges > num_of_nodes*(num_of_nodes-1)/2):
        print('to many edges, impossible to generate simple graph')
        return 

    adj_matrix = np.zeros((num_of_nodes,num_of_nodes))
    for _ in range(num_of_edges):
        empty_edges = []
        for i,row in enumerate(adj_matrix):
            for j,col in enumerate(row):
                if j>i and adj_matrix[i,j] == 0:
                    empty_edges.append([i,j])
        x,y = random.choice(empty_edges)
        adj_matrix[x,y],adj_matrix[y,x] = 1,1
    return adj_matrix_to_nx_graph_object(adj_matrix)


def rand_graph_edge_prob(num_of_nodes,prob):
    adj_matrix = np.zeros((num_of_nodes,num_of_nodes))
    for i in range (num_of_nodes):
        for j in range(i+1,num_of_nodes):
            adj_matrix[i,j] = int(random.random() < prob)
            adj_matrix[j,i] = adj_matrix[i,j]
    return adj_matrix