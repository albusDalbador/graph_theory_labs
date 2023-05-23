import matplotlib.pyplot as plt
from lab4.digraph import *

def main():
    ##### zad 4.1

    n = 5  # liczba wierzchołków
    p = 0.5  # prawdopodobieństwo istnienia krawędzi

    G = generate_digraph(n, p)
    print("generated digraph:")
    print(G.edges())

    nx.draw_circular(G,with_labels=True)
    plt.show()

    #####




if __name__ == '__main__':
    main()
