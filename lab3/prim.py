import numpy as np
import networkx as nx
import matplotlib.pyplot as plt 


# zad 3.5 
def get_min_spanning_tree(G): # algorytm prima
    visited_nodes = [list(G)[0]]
    spanning_edges = []
    while len(visited_nodes) != G.number_of_nodes():

        u,v = -1,-1
        edge_weight = np.inf
        for node in visited_nodes:
            for neighbor in G.neighbors(node):
                if neighbor not in visited_nodes and G.get_edge_data(node,neighbor)['weight'] < edge_weight:
                    u,v = node,neighbor
                    edge_weight = G.get_edge_data(u,v)['weight']
        
        visited_nodes.append(v)
        spanning_edges.append((u,v,{'weight' :edge_weight}))

    return spanning_edges

def visualise_spanning_tree(G,spanning_tree):
    plt.figure(figsize=[10.6,7.2])

    plt.subplot(1,2,1)
    nx.draw_circular(G,with_labels=True)
    nx.draw_networkx_edge_labels(G,pos=nx.circular_layout(G),edge_labels=nx.get_edge_attributes(G,'weight'))

    G = nx.create_empty_copy(G)
    for edge in spanning_tree:
        G.add_edge(edge[0],edge[1])
        G[edge[0]][edge[1]]['weight'] = edge[2]['weight']

    plt.subplot(1,2,2)    
    nx.draw_circular(G,with_labels=True)
    nx.draw_networkx_edge_labels(G,pos=nx.circular_layout(G),edge_labels=nx.get_edge_attributes(G,'weight'))





# def prim_algorithm(graph):
    
#     mst_vertices = []
#     min_edge_weights = {}
#     parents = {}
    
#     for i in range(len(graph)):
#         min_edge_weights[i] = float('inf')
#         parents[i] = None
    
#     min_edge_weights[0] = 0
    
#     while len(mst_vertices) < len(graph):
#         min_weight_vertex = None
#         for i in range(len(graph)):
#             if i not in mst_vertices:
#                 if min_weight_vertex is None or min_edge_weights[i] < min_edge_weights[min_weight_vertex]:
#                     min_weight_vertex = i
        
#         mst_vertices.append(min_weight_vertex)
        
#         for i in range(len(graph)):
#             if graph[min_weight_vertex][i] != 0 and i not in mst_vertices:
#                 if graph[min_weight_vertex][i] < min_edge_weights[i]:
#                     min_edge_weights[i] = graph[min_weight_vertex][i]
#                     parents[i] = min_weight_vertex
    

#     mst_edges = []
#     total_weight = 0
    
#     for i in range(1, len(graph)):
#         mst_edges.append((parents[i], i))
#         total_weight += graph[parents[i]][i]
    
#     return mst_edges, total_weight