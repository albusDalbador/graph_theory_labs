import numpy as np


def adj_list_to_inc_matrix(adj_list):
    num_of_nodes = adj_list.shape[0]
    inc_matrix = np.zeros((num_of_nodes,num_of_nodes),dtype=np.int32)
    for node,list_of_adjacents in enumerate(adj_list):
        for adjacent in list_of_adjacents:
            inc_matrix[node,adjacent],inc_matrix[adjacent,node] = 1,1
    return inc_matrix



def adj_list_to_adj_matrix(adj_list):
    return inc_matrix_to_adj_matrix(adj_list_to_inc_matrix(adj_list))


def inc_matrix_to_adj_matrix(inc_matrix):
    num_of_nodes = inc_matrix.shape[0]
    adj_matrix = []
    for i in range (num_of_nodes):
        for j in range (i,num_of_nodes -1):
            if inc_matrix[i,j] == 1:
                step_row = [0]*num_of_nodes
                step_row[i],step_row[j] = 1,1
                adj_matrix.append(step_row)
    return np.transpose(adj_matrix)


def inc_matrix_to_adj_list(inc_matrix):
    return adj_matrix_to_adj_list(inc_matrix_to_adj_matrix(inc_matrix))


def adj_matrix_to_adj_list(adj_matrix):
    num_of_nodes = adj_matrix.shape[0]
    adj_list = [[] for _ in range (num_of_nodes)]
    adj_matrix = np.transpose(adj_matrix)
    for line in adj_matrix:
        i,j = np.nonzero(line)[0]
        adj_list[i].append(j)
        adj_list[j].append(i)
    return np.array(adj_list,dtype=object)



def adj_matrix_to_inc_matrix(adj_matrix):
    return adj_list_to_inc_matrix(adj_matrix_to_adj_list(adj_matrix))

#incidence matrix
#adjacency matrix 
#adjacency list