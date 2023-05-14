from lab1.graph_random import *
from lab2.graph_metrics import find_biggest_component
from lab3.dijkstra import *

import numpy as np 
import matplotlib.pyplot as plt

# def is_graph_connected(graph):
#     visited = set()
#     stack = [0]

#     while stack:
#         vertex = stack.pop()
#         if vertex not in visited:
#             visited.add(vertex)
#             for neighbor_idx, neighbor_value in enumerate(graph[vertex]):
#                 if neighbor_value == 1 and neighbor_idx not in visited:
#                     stack.append(neighbor_idx)

#     return len(visited) == len(graph)



# def rand_connected_graph(number_of_nodes,number_of_edges):
#     visited = False
#     if(number_of_edges<number_of_nodes-1):
#         print("number of edges must be higher than node - 1 otherwise graph will be always not connected")
#         return visited,rand_graph_edge_num(number_of_nodes,number_of_edges)
#     if (number_of_edges > number_of_nodes*(number_of_nodes-1)/2):
#         return visited,rand_graph_edge_num(number_of_nodes,number_of_edges)
    
#     while visited == False:
#         adj_matrix = rand_graph_edge_num(number_of_nodes,number_of_edges)
#         visited=is_graph_connected(adj_matrix)
#     return visited, adj_matrix



# def add_random_weights(graph):
#     n = len(graph)
#     weighted_graph = [[0 for _ in range(n)] for _ in range(n)]
#     for i in range(n):
#         for j in range(n):
#             if graph[i][j] == 1:
#                 weight = random.randint(1, 10)
#                 weighted_graph[i][j] = weight
#     return weighted_graph



# def dijkstra(G, source):
#     # n = len(graph)
#     unvisited = set(range(G.number_of_nodes()))
#     distances = [np.inf] * G.number_of_nodes()
#     distances[source] = 0
#     predecessors = [None] * G.number_of_nodes()

#     while unvisited:
#         current = min(unvisited, key=lambda vertex: distances[vertex])
#         unvisited.remove(current)

#         for neighbor, weight in enumerate(G.nodes[current]):
#             if weight and neighbor in unvisited:
#                 new_distance = distances[current] + weight
#                 if new_distance < distances[neighbor]:
#                     distances[neighbor] = new_distance
#                     predecessors[neighbor] = current

#     return distances, predecessors
    

    
# zad 3.1
def generate_wieghted_graph(num_of_nodes=10,num_of_edges=25,weight_range=[1,10]):
    graph = rand_connected_graph(num_of_nodes,num_of_edges)
    if graph:
        for _,_,data in graph.edges(data=True):
            data['weight'] = np.random.randint(weight_range[0],weight_range[1])
    return graph

def rand_connected_graph(num_of_nodes=10,num_of_edges=25):
    step_graph = rand_graph_edge_num(num_of_nodes,num_of_edges)
    return find_biggest_component(step_graph)


# zad 3.3
def get_graph_dist_matrix(G):
    matrix = []
    for source in G.nodes():
        dist,_ = invoke_dijkstra_alg(G,source)
        matrix.append(dist)
    return np.array(matrix)


# zad 3.4
def get_graph_centre(G):
    dist_matrix = get_graph_dist_matrix(G)
    return np.argmin([np.sum(x) for x in dist_matrix])

def get_graph_minimax(G):
    dist_matrix = get_graph_dist_matrix(G)
    return np.argmin([np.max(x) for x in dist_matrix])


