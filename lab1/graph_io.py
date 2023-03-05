import numpy as np


def read_inc_matrix_shape(filename='input.txt'):
    inc_matrix = [] 
    with open(filename,'r') as inc_matrix_input:
        for row in inc_matrix_input:
            inc_matrix.append(row.split(' '))
    return np.array(inc_matrix,dtype=np.int8)


def read_adj_matrix_shape(filename='input.txt'):
    adj_matrix = [] 
    with open(filename,'r') as adj_matrix_input:
        for row in adj_matrix_input:
            adj_matrix.append(row.split(' '))
        for row in adj_matrix_input:
            adj_matrix.append(row.split(' '))
    return np.array(adj_matrix,dtype=np.int8)


def read_adj_list_shape(filename='input.txt'):
    adj_list = [] 
    with open(filename,'r') as adj_list_input:
        for row in adj_list_input:
            adj_list.append([int(item) for item in row.split(' ')])
    return np.array(adj_list,dtype=object)

#to save array use numpy.savetxt()