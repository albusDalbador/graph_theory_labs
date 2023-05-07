from .graph_metrics import check_if_seq_is_graph

import numpy as np 


def generate_graph_from_seq(arr):
    if not check_if_seq_is_graph(arr):
        print('Podany ciąg stopni wierzchołków nie jest poprawny')
        return None
    
    arr = np.flip(np.sort(arr))
    adj_list = [[] for _ in arr]
    power_list = list(map(lambda x: list(x),list(zip(np.arange(0,arr.size),arr))))
    while np.count_nonzero(list(map(lambda x: x[1],power_list))):
        for ind in range(1,power_list[0][1] + 1):
            power_list[0][1] -= 1
            power_list[ind][1] -= 1
            adj_list[power_list[ind][0]].append(power_list[0][0])
            adj_list[power_list[0][0]].append(power_list[ind][0])
        power_list = list(filter(lambda x: x[1] != 0,power_list))
    return adj_list
