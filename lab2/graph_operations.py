from .graph_metrics import check_if_seq_is_graph
from lab1.shape_conversion import adj_list_to_nx_graph_object, inc_matrix_to_nx_graph_object,nx_graph_object_to_inc_matrix

import numpy as np 
import networkx as nx 
import random


# zad 2.1
def generate_graph_from_seq(arr):
    if not check_if_seq_is_graph(arr):
        print('Podany ciąg stopni wierzchołków nie jest poprawny')
        return None
    
    arr = np.flip(np.sort(arr))
    adj_list = [[] for _ in arr]
    power_list = list(map(lambda x: list(x),list(zip(np.arange(0,arr.size),arr))))
    while np.count_nonzero(list(map(lambda x: x[1],power_list))):
        for ind in range(1,power_list[0][1] + 1):
            power_list[0][1] -= 1
            power_list[ind][1] -= 1
            adj_list[power_list[ind][0]].append(power_list[0][0])
            adj_list[power_list[0][0]].append(power_list[ind][0])
        power_list = list(filter(lambda x: x[1] != 0,power_list))
        power_list = sorted(power_list,key=lambda x : x[1], reverse=True)

    return adj_list_to_nx_graph_object(adj_list)


# zad 2.2
def randomize_graph(G,num_of_swaps=10):
    inc_matrix = nx_graph_object_to_inc_matrix(G)
    inc_matrix = np.transpose(inc_matrix)

    for _ in range(num_of_swaps):
        first_edge_ind,second_edge_ind = np.random.choice(np.arange(0,len(inc_matrix)),size=2,replace=False)
        a,b = np.nonzero(inc_matrix[first_edge_ind])[0]
        c,d = np.nonzero(inc_matrix[second_edge_ind])[0]

        if a != d and b != c:
            inc_matrix[first_edge_ind][[a,b]] = 0
            inc_matrix[first_edge_ind][[a,d]] = 1
            inc_matrix[second_edge_ind][[c,d]] = 0
            inc_matrix[second_edge_ind][[b,c]] = 1

    return inc_matrix_to_nx_graph_object(np.transpose(inc_matrix))


# zad 2.3
def find_biggest_component(G):
    adj_list = [[x[0] for x in G.adj[node].items()] for node in G.adj]
    
    comp_list = np.full(len(list(adj_list)),-1)
    comp_num = 0
    for ind,node in enumerate(adj_list):
        if comp_list[ind] == -1:
            comp_num += 1
            comp_list[ind] = comp_num
            comp_list = find_biggest_component_rec(comp_num,node,adj_list,comp_list)

    biggest_ind = np.argmax(np.bincount(comp_list))
    biggest_comp_adj_list = [adj_list[ind] for ind in np.asarray(comp_list == biggest_ind).nonzero()[0]]
    
    return adj_list_to_nx_graph_object(biggest_comp_adj_list)


def find_biggest_component_rec(comp_num,node,adj_list,comp_list):
    for neighbour in node:
        if comp_list[neighbour] == -1:
            comp_list[neighbour] = comp_num
            comp_list = find_biggest_component_rec(comp_num,adj_list[neighbour],adj_list,comp_list)
    return comp_list


# zad 2.4
def generate_euler_graph(num_of_nodes=10):
    node_degrees = np.random.randint(1,(num_of_nodes-1)/2,num_of_nodes)*2
    while not check_if_seq_is_graph(node_degrees): 
        node_degrees = np.random.randint(1,(num_of_nodes-1)/2,num_of_nodes)*2

    return find_biggest_component(generate_graph_from_seq(node_degrees))
    
    # node_degrees = [1]
    # while not check_if_seq_is_graph(node_degrees):
    #     for _ in range (num_of_nodes):
    #         power = random.randint(1,(num_of_nodes-1)/2)*2
    #         node_degrees.append(power)

    # return find_biggest_component()
