from graph_random import *
from shape_converstion import *
from graph_io import *
from graph_draw import *

import matplotlib.pyplot as plt


inc_matrix = read_inc_matrix_shape()
# adj_matrix = read_adj_matrix_shape()
# adj_list = read_adj_list_shape()

print(inc_matrix)
# print(adj_matrix)
# print(adj_list)

adj_matrix = inc_matrix_to_adj_matrix(inc_matrix=inc_matrix)
adj_list = adj_matrix_to_adj_list(adj_matrix)
inc_matrix = adj_list_to_inc_matrix(adj_list)
print(inc_matrix)

adj_matrix = adj_list_to_adj_matrix(adj_list)
print(adj_matrix)
inc_matrix = adj_matrix_to_inc_matrix(adj_matrix)
print(inc_matrix)
adj_list = inc_matrix_to_adj_list(inc_matrix)
print(adj_list)

############

plt.figure()
draw_from_adj_matrix(adj_matrix)
plt.figure()
draw_from_inc_matrix(inc_matrix)
plt.figure()
draw_from_adj_list(adj_list)

plt.show()