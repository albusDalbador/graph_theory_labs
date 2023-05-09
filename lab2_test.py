print('program started')
import sys
sys.path.append('.')

print('import started')
import matplotlib.pyplot as plt
from random import choice
import networkx as nx 

print('local improt started')
from lab2.graph_metrics import * 
from lab2.graph_operations import *
print('import finished')

# print(good_seq)
# print([n for n in test_graph.neighbors(0)])
# print(list(test_graph.nodes())[0])
##### zad 2.1

# good_seq = [1, 3, 2, 3, 2, 4, 1]
# print(check_if_seq_is_graph([1, 3, 2, 3, 2, 4, 1]))

# print(check_if_seq_is_graph([1, 3, 3, 4, 2, 3, 1]))

# print(check_if_seq_is_graph([6, 2, 4, 2, 6, 6, 6, 4, 4, 4]))
# print(check_if_seq_is_graph([1,1]))
# print(check_if_seq_is_graph([2,2]))
# test_graph = generate_graph_from_seq(good_seq)

# nx.draw_circular(test_graph, with_labels=True)
# plt.show()

# generate_graph_from_seq([6, 2, 4, 2, 6, 6, 6, 4, 4, 4])

##### 

##### zad 2.2

# good_seq = [1, 3, 2, 3, 2, 4, 1]
# test_graph = generate_graph_from_seq(good_seq)

# plt.subplot(1,2,1)
# nx.draw_circular(test_graph)

# randomized_graph = randomize_graph(test_graph)

# plt.subplot(1,2,2)
# nx.draw_circular(randomized_graph)

#####

###### zad 2.3

# good_seq = [1, 3, 2, 3, 2, 4, 1]
# test_graph = generate_graph_from_seq(good_seq)

# plt.subplot(1,2,1)
# nx.draw_circular(test_graph, with_labels=True)

# biggest_component = find_biggest_component(test_graph)
# print(biggest_component)

# plt.subplot(1,2,2)
# nx.draw_circular(biggest_component, with_labels=True)

#####

##### zad 2.4

# euler_graph = generate_euler_graph(num_of_nodes=10)

# nx.draw_circular(euler_graph,with_labels=True)

# graph = euler_graph.copy()

# euler_path=find_euler_path(euler_graph)
# print(euler_path)

##### zad 2.5

# k_regular_graph = generate_k_regular_graph()

# nx.draw_circular(k_regular_graph)

#####

##### zad 2.6

# k_regular_graph = generate_k_regular_graph()
# hamilton_path = find_hamilton_path_rec(k_regular_graph,0)
# print(hamilton_path)
# plt.subplot(2,1,1)
# nx.draw_circular(k_regular_graph,with_labels=True)

# random_graph = rand_graph_edge_num(10,10)
# hp = find_hamilton_path_rec(random_graph,0)
# print(hp)
# plt.subplot(2,1,2)
# nx.draw_circular(random_graph,with_labels=True)

##### 
plt.show()