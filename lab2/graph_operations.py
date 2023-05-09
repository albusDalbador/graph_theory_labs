from .graph_metrics import *
from lab1.shape_conversion import adj_list_to_nx_graph_object

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
def randomize_graph(G,num_of_swaps=10): # mozna zastapic nx.double_edge_swap(G)
    for _ in range (num_of_swaps):
        G_step = swap_edges(G.copy())
        while not np.array_equal([len(G[v]) for v in G],[len(G_step[v]) for v in G]):
            G_step = swap_edges(G.copy())
        G = G_step
    return G


def swap_edges(G):
    edge1,edge2 = random.sample(list(G.edges()),2)
    
    while edge1 == edge2 or edge1[0] == edge2[0] or edge1[1] == edge2[1]:
        edge2 = random.choice(list(G.edges()))
    
    if len(set([edge1[0], edge1[1], edge2[0], edge2[1]])) != 4:
        return G
    
    G.remove_edges_from([edge1, edge2])
    G.add_edges_from([(edge1[0], edge2[1]), (edge2[0], edge1[1])])
    
    return G


# zad 2.4
def generate_euler_graph(num_of_nodes=10):
    node_degrees = np.random.randint(1,(num_of_nodes+1)/2,num_of_nodes)*2
    while not check_if_seq_is_graph(node_degrees): 
        node_degrees = np.random.randint(1,(num_of_nodes-1)/2,num_of_nodes)*2

    return find_biggest_component(randomize_graph(generate_graph_from_seq(node_degrees)))


# zad 2.5
def generate_k_regular_graph(num_of_nodes=10,node_power=5):
    if num_of_nodes <= node_power:
        print("Liczba wierzchołków musi być większa od ich stopnia")
        return None
    if node_power % 2 == 1 and num_of_nodes % 2 == 1:
        print("Jeśli stopień jest nieparzysty, to liczba wierzchołków musi być parzysta")
        return None

    k_regular_graph = generate_graph_from_seq([node_power] * num_of_nodes)

    return randomize_graph(k_regular_graph,num_of_swaps=num_of_nodes*2)



