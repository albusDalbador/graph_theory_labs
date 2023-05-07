import numpy as np 


def check_if_seq_is_graph(arr) -> bool:
    arr = np.flip(np.sort(arr))
    while True:
        if not np.count_nonzero(arr):
            return True
        if arr[0] > arr.size or np.extract(arr < 0, arr).size > 0:
            return False

        arr = [0] + [item-1 for ind,item in enumerate(arr) if ind > 0 and ind <= arr[0]] + [item for ind,item in enumerate(arr) if ind > arr[0]]

        arr = np.flip(np.sort(arr))



