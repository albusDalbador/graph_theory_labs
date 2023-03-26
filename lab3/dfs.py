from graph_random import *
import random

def is_graph_connected(graph):
    visited = set()
    stack = [0]

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            for neighbor_idx, neighbor_value in enumerate(graph[vertex]):
                if neighbor_value == 1 and neighbor_idx not in visited:
                    stack.append(neighbor_idx)

    return len(visited) == len(graph)



def rand_connected_graph(number_of_nodes,number_of_edges):
    visited = False
    if(number_of_edges<number_of_nodes-1):
        print("number of edges must be higher than node - 1 otherwise graph will be always not connected")
        return visited,rand_graph_edge_num(number_of_nodes,number_of_edges)
    if (number_of_edges > number_of_nodes*(number_of_nodes-1)/2):
        return visited,rand_graph_edge_num(number_of_nodes,number_of_edges)
    
    while visited == False:
        adj_matrix = rand_graph_edge_num(number_of_nodes,number_of_edges)
        visited=is_graph_connected(adj_matrix)
    return visited, adj_matrix



def add_random_weights(graph):
    n = len(graph)
    weighted_graph = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                weight = random.randint(1, 10)
                weighted_graph[i][j] = weight
    return weighted_graph



def dijkstra(graph, source):
    n = len(graph)
    unvisited = set(range(n))
    distances = [np.inf] * n
    distances[source] = 0
    predecessors = [None] * n

    while unvisited:
        current = min(unvisited, key=lambda vertex: distances[vertex])
        unvisited.remove(current)

        for neighbor, weight in enumerate(graph[current]):
            if weight and neighbor in unvisited:
                new_distance = distances[current] + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    predecessors[neighbor] = current

    return distances, predecessors
    