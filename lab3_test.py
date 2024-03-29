from lab1.graph_random import *
from lab1.graph_draw import *
from lab3.dfs import *
from lab3.prim import *
from lab3.dijkstra import *
import matplotlib.pyplot as plt



##### zad 3.1

# G = generate_wieghted_graph(num_of_nodes=7,num_of_edges=15)

# nx.draw_circular(G,with_labels=True)
# nx.draw_networkx_edge_labels(G,pos=nx.circular_layout(G),edge_labels=nx.get_edge_attributes(G,'weight'))

#####

##### zad 3.2

# G = generate_wieghted_graph(num_of_nodes=7,num_of_edges=15)

# nx.draw_circular(G,with_labels=True)
# nx.draw_networkx_edge_labels(G,pos=nx.circular_layout(G),edge_labels=nx.get_edge_attributes(G,'weight'))

# for source in G.nodes():
#     dist,pred = invoke_dijkstra_alg(G,source)
#     print(dist,pred)

#####

##### zad 3.3

# for _ in range(20):
#     G = generate_wieghted_graph(num_of_nodes=7,num_of_edges=15)
#     dist_matrix = get_graph_dist_matrix(G)
#     print(dist_matrix,'\n-------------------')

#####

##### zad 3.4

# G = generate_wieghted_graph(num_of_nodes=7,num_of_edges=15)
# nx.draw_circular(G,with_labels=True)
# nx.draw_networkx_edge_labels(G,pos=nx.circular_layout(G),edge_labels=nx.get_edge_attributes(G,'weight'))

# center = get_graph_centre(G)
# minimax = get_graph_minimax(G)
# dist_matrix = get_graph_dist_matrix(G)

# print(center,minimax)
# print(dist_matrix)

#####

##### zad 3.5

# G = generate_wieghted_graph(num_of_nodes=7,num_of_edges=15)

# spanning_tree = get_min_spanning_tree(G)
# print(spanning_tree)

# visualise_spanning_tree(G,spanning_tree)

#####

plt.show()









# number_of_nodes = 6
# number_of_edges = 8
# answer,adj_matrix = rand_connected_graph(number_of_nodes,number_of_edges) 
# if answer: 
#     weigths = add_random_weights(adj_matrix)
#     # print(weigths)
#     plt.figure()
#     draw_from_adj_matrix(adj_matrix,weigths)
    
#     all_distances = []
#     sum_of_row = []
#     maxmin_of_row = []
#     for i in range(0,number_of_nodes):
#         distances, predecessors = dijkstra(weigths,i)
#         all_distances.append(distances)
#         sum_of_row.append(sum(distances))
#         maxmin_of_row.append(max(distances))
#         # print("Distances:", distances)
#         # print("Predecessors:", predecessors)
#     # path = []
#     # current = 4
#     # while current is not None:
#     #     path.append(current)
#     #     current = predecessors[current]
#     # path.reverse()
#     # print("Shortest path to vertex 4:", path)
#     for row in all_distances:
#         print(row)

#     print(sum_of_row)
#     print(maxmin_of_row)
#     sum_index = sum_of_row.index(min(sum_of_row))
#     maxmin_index = maxmin_of_row.index(min(maxmin_of_row))
#     print("Centrum grafu to wierzchołek o indeksie: ", sum_index)
#     print("Centrum minimax grafu to wierzchołek o indeksie: ", maxmin_index)

#     # Find the minimum spanning tree
#     mst_edges, total_weight = prim_algorithm(weigths)

#     # Print the edges in the minimum spanning tree and the total weight
#     print("Edges in the minimum spanning tree:", mst_edges)
#     print("Total weight of the minimum spanning tree:", total_weight)
#     plt.show()
        
    


