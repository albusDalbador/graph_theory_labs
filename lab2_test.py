import sys

from networkx import is_isomorphic
sys.path.append('.')

import matplotlib.pyplot as plt
from random import choice

from lab2.graph_metrics import * 
from lab2.graph_operations import *
from lab1.graph_draw import *


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

# plt.subplot(1,2,1)
# nx.draw_circular(test_graph)

# randomized_graph = randomize_graph(test_graph)

# plt.subplot(1,2,2)
# nx.draw_circular(randomized_graph)

# biggest_component = find_biggest_component(test_graph)

# print(np.asarray(biggest_component == 1).nonzero())
#####

###### zad 2.3

# plt.subplot(1,2,1)
# nx.draw_circular(test_graph, with_labels=True)
# plt.subplot(1,2,2)
# nx.draw_circular(biggest_component, with_labels=True)

# plt.show()

######

##### zad 2.4

euler_graph = generate_euler_graph()
# nx.draw_circular(euler_graph)
# plt.show()
# lista kolejności odwiedzania wierzchołków
# euler_path = find_euler_path(euler_graph)

graph = euler_graph

euler_path = []
while True:
    node = random.choice(list(graph))
    # print(node)
    if len(graph.edges(node)) > 1:
        for edge in graph.edges(node):
            test_graph = graph.copy()
            # test_graph.remove_edge(*edge)
            if test_graph.nodes() == find_biggest_component(test_graph).nodes():
                print('isomorphic')
                euler_path.append(edge[0])
                graph.remove_edge(*edge)
                break
    else:
        edge = list(graph.edges(node))[0]
        euler_path.append(edge[0])
        graph.remove_edge(*edge)

    print(graph)
    if nx.is_empty(graph):
        # return euler_path
        print(euler_path)
        break


plt.show()
