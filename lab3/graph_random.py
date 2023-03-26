from random import random
import numpy as np
import random


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
    return adj_matrix

