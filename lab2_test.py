import sys
sys.path.append('.')

from lab2.graph_metrics import * 
from lab2.graph_operations import *
from lab1.graph_draw import *


print(check_if_seq_is_graph([1, 3, 2, 3, 2, 4, 1]))

print(check_if_seq_is_graph([1, 3, 3, 4, 2, 3, 1]))

# print(is_degree_sequence({1, 3, 2, 3, 2, 4, 1}))

# print(is_degree_sequence({1, 3, 3, 4, 2, 3, 1}))

