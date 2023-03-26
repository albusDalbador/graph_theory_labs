import networkx as nx


def draw_from_adj_matrix(adj_matrix,weights):
    g = nx.Graph(directed=False)
    num_of_nodes = adj_matrix.shape[0]

    for ind in range(num_of_nodes):
        g.add_node(ind)
    
    for i in range(num_of_nodes):
        for j in range(i+1,num_of_nodes):
            if adj_matrix[i,j] == 1:
                g.add_edge(i,j,weight=weights[j][i])
                

    pos = nx.shell_layout(g)
    nx.draw(g, pos, with_labels=True, font_weight='bold')
    labels = nx.get_edge_attributes(g, 'weight')
    nx.draw_networkx_edge_labels(g, pos, edge_labels=labels, font_weight='bold')    
    

    

