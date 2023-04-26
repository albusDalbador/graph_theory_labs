import numpy as np


def adj_list_to_inc_matrix(adj_list): # adj_list_to_adj_matrix
    # dla wygody i lepszej czytelności zapisujemy ilość węzłów w przetwarzanym grafie
    num_of_nodes = adj_list.shape[0]
    # inicjujemy macierz sąsiedstwa wypełnioną zerami
    inc_matrix = np.zeros((num_of_nodes,num_of_nodes),dtype=np.int32)
    # przechodzimy po liście sąsiedstwa
    for node,list_of_adjacents in enumerate(adj_list):
        # przechodzimy po wszystkih sąsiadach danego wierzchołka
        for adjacent in list_of_adjacents:
            # ustawiamy jedynki na pozycjach odpowiadacjącym krawędzi łączącej wierzchołki
            inc_matrix[node,adjacent],inc_matrix[adjacent,node] = 1,1
    return inc_matrix



def adj_list_to_adj_matrix(adj_list): #inna nazwa
    return inc_matrix_to_adj_matrix(adj_list_to_inc_matrix(adj_list))


def inc_matrix_to_adj_matrix(inc_matrix): # naodwrót
    # dla wygody i lepszej czytelności zapisujemy ilość węzłów w przetwarzanym grafie
    num_of_nodes = inc_matrix.shape[0]
    # macierz incydencji pierwotnie nie zawiera elementów
    adj_matrix = []
    # przechodzimy po wszystkich elementach w "górnym trójkącie" macierzy incydencji
    for i in range (num_of_nodes):
        for j in range (i,num_of_nodes -1):
            # napotkanie jedynki oznacza, że wierzchołek 'i' jest połączony z wierzchołkiem 'j'
            if inc_matrix[i,j] == 1:
                # tworzymy nową krawędź i dodajemy ją do listy incydencji
                step_row = [0]*num_of_nodes
                step_row[i],step_row[j] = 1,1
                adj_matrix.append(step_row)
    # tansponujemy macierz by uzyskać bardziej 'kanoniczną' postać, gdzie krawędzi są umieszczone pionowo
    return np.transpose(adj_matrix)


def inc_matrix_to_adj_list(inc_matrix): # inna nazwa
    return adj_matrix_to_adj_list(inc_matrix_to_adj_matrix(inc_matrix))


def adj_matrix_to_adj_list(adj_matrix): # inc_matrix_to_adj_list
    # dla wygody i lepszej czytelności zapisujemy ilość węzłów w przetwarzanym grafie
    num_of_nodes = adj_matrix.shape[0]
    # inicjujemy listę sąsiedstwa 
    adj_list = [[] for _ in range (num_of_nodes)]
    # dla wygodniejszego przetwarzania transponujemy macierz 
    adj_matrix = np.transpose(adj_matrix)
    for line in adj_matrix:
        # znajdujemy wierzchołki, które łączy dana krawędź i dodajemy je do odpowiednich list
        i,j = np.nonzero(line)[0]
        adj_list[i].append(j)
        adj_list[j].append(i)
    return np.array(adj_list,dtype=object)



def adj_matrix_to_inc_matrix(adj_matrix): # inna nazwa
    return adj_list_to_inc_matrix(adj_matrix_to_adj_list(adj_matrix)) 

#incidence matrix
#adjacency matrix 
#adjacency list
