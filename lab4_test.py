import matplotlib.pyplot as plt
from lab4.digraph import *
from lab4.kosaraju import *
from lab4.di_shape_conversion import *
from lab4.digraph_io import *
from lab4.bellman_ford import *
from lab4.jhonson import johnson_algorithm

def main():
    ##### zad 4.1
    print("zad 4.1")

    n = 5  # liczba wierzchołków
    p = 0.5  # prawdopodobieństwo istnienia krawędzi
    digraph = generate_random_digraph(n, p)

    # digraph = read_digraph_from_adj_matrix()
    # digraph = read_digraph_from_adjacency_list()
    # digraph = read_digraph_from_inc_matrix()

    print("generated digraph:")
    inc_matrix = nx_digraph_object_to_inc_matrix(digraph)
    adj_matrix = nx_digraph_object_to_adj_matrix(digraph)
    adj_list = nx_digraph_object_to_adj_list(digraph)

    print('\nIncidence matrix\n', inc_matrix)
    print('\nAdjacency matrix\n', adj_matrix)
    print('\nAdjacency list')
    for i in range(len(adj_list)):
        print(f'Vertex {i}: {adj_list[i]}')

    # nx.draw_circular(digraph, with_labels=True)
    # plt.show()

    #####

    ##### zad 4.2
    print("\nzad 4.2")

    scc = kosaraju(digraph)
    # Silnie spójne składowe
    print("Strongly coherent components:")
    for i, component in enumerate(scc, 1):
        print(f"Składowa {i}, wierzchołki: {component}")

    nx.draw_circular(digraph, with_labels=True)
    plt.show()

    #####

    ##### zad 4.3
    print("\nzad 4.3")
    
    n = 5
    p = 0.5
    digraph = generate_random_digraph_with_weight(n, p)

    # Perform Bellman-Ford algorithm from a given source vertex
    shortest_distance = bellman_ford(digraph, 0)

    print("Shortest distance from 0 vertex:")
    print(shortest_distance)

    #####

    ##### zad 4.4
    print("\nzad 4.4")

    distances = johnson_algorithm(digraph)

    print("Matrix of shortest distances:")
    print(distances)

    visualize_digraph_with_weights(digraph)


if __name__ == '__main__':
    main()
