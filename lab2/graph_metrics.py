import numpy as np 
import random
from lab1.shape_conversion import *

# zad 2.1
def check_if_seq_is_graph(arr) -> bool:
    arr = np.flip(np.sort(arr),0)
    while True:
        if not np.count_nonzero(arr):
            return True
        if arr[0] >= arr.size or np.extract(arr < 0, arr).size > 0:
            return False

        arr = [0] + [item-1 for ind,item in enumerate(arr) if ind > 0 and ind <= arr[0]] + [item for ind,item in enumerate(arr) if ind > arr[0]]
        arr = np.flip(np.sort(arr),0)


# zad 2.3
def find_biggest_component(G):
    comp_num = 0
    comp_list = np.full(len(list(G.nodes())),-1)

    for node in list(G.nodes()):
        if comp_list[node] == -1:
            comp_num += 1
            comp_list[node] = comp_num
            comp_list = find_biggest_component_rec(comp_num,node,G,comp_list)
    
    biggest_ind = np.argmax(np.bincount(comp_list))
    biggest_comp_list = [list(G.nodes())[ind] for ind in list(np.asarray(comp_list == biggest_ind).nonzero())[0]]

    for node in list(G.nodes()):
        if node not in biggest_comp_list:
            G.remove_node(node)

    return G


def find_biggest_component_rec(comp_num,node,G,comp_list):
    for neighbor in list(G.neighbors(node)):
        if comp_list[neighbor] == -1:
            comp_list[neighbor] = comp_num
            find_biggest_component_rec(comp_num,neighbor,G,comp_list)
    return comp_list


# zad 2.4
def find_euler_path(graph):
    euler_path = []
    node = random.choice(list(graph))

    while True:
        for edge in graph.edges(node):
            test_graph = graph.copy()
            test_graph.remove_edge(*edge)
            
            if test_graph.nodes() == find_biggest_component(test_graph).nodes():
                node=edge[1]
                euler_path.append(edge[0])
                graph.remove_edge(*edge)
                break
        
        if graph.degree(node) == 1:
            edge = list(graph.edges(node))[0]
            node=edge[1]
            euler_path.append(edge[0])
            graph.remove_edge(*edge)

        if nx.is_empty(graph):
            print(graph)
            return euler_path
    

#zad 2.6
def find_hamilton_path_rec(G, node, path=[]):
    if node not in set(path):
        path.append(node)
        
        if len(path)==G.number_of_nodes():
            return path
        
        for neighbor in list(G.neighbors(node)):
            candidate = find_hamilton_path_rec(G,  neighbor, path)
            
            if candidate is not None:  
                return candidate
    else:
        return None
