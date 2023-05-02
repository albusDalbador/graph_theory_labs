from graph_random import *
from shape_conversion import *
from graph_io import *
from graph_draw import *
import matplotlib.pyplot as plt


inc_matrix = read_inc_matrix_shape('inc_matrix.txt')
adj_matrix = read_adj_matrix_shape('adj_matrix.txt')
adj_list = read_adj_list_shape('adj_list.txt')


adj_matrix = inc_matrix_to_adj_matrix(inc_matrix)
print(adj_matrix)

adj_list = adj_matrix_to_adj_list(adj_matrix)
print(adj_list)

inc_matrix = adj_list_to_inc_matrix(adj_list)
print(inc_matrix)


adj_matrix = adj_list_to_adj_matrix(adj_list)
print(adj_matrix)

inc_matrix = adj_matrix_to_inc_matrix(adj_matrix)
print(inc_matrix)

adj_list = inc_matrix_to_adj_list(inc_matrix)
print(adj_list)


plt.figure()

plt.subplot(2,2,1)
plt.title('Z macierzy sąsiedstwa')
draw_from_adj_matrix(adj_matrix)

plt.subplot(2,2,2)
plt.title('Z macierzy incydencji')
draw_from_inc_matrix(inc_matrix)

plt.subplot(2,2,3)
plt.title('Z listy sąsiedstwa')
draw_from_adj_list(adj_list)


plt.figure(figsize=(10.8,4.8))

random_adj_matrix = rand_graph_edge_num(num_of_nodes=8,num_of_edges=10)
plt.subplot(1,2,1)
plt.title('Graf losowy o ustalonej ilości krawędzi')
draw_from_adj_matrix(random_adj_matrix)

random_adj_matrix = rand_graph_edge_prob(num_of_nodes=8,prob=0.5)
plt.subplot(1,2,2)
plt.title('Graf losowy o zadanym prawdopodobieństwie istnienia krawędzi')
draw_from_adj_matrix(random_adj_matrix)


plt.show()
