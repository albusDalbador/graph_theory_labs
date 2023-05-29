import numpy as np
import networkx as nx 
import matplotlib.pyplot as plt


##### zad 1

def generate_flow_network(num_of_layers=3):
    G = nx.DiGraph(num_of_layers=num_of_layers)
    G.add_node('source',layer=0)

    for layer in range(1,num_of_layers+1):
        num_of_nodes = np.random.randint(2,num_of_layers)
        for node in range(num_of_nodes):
            G.add_node(f'%d_%d'%(layer,node),layer=layer)

    G.add_node('target',layer=num_of_layers+1)

    # poprawne polaczenia pomiedzy wszystkimi warstwami
    for step in range(num_of_layers + 1):
        prev_layer = [node for node,data in G.nodes(data=True) if data['layer'] == step]
        next_layer = [node for node,data in G.nodes(data=True) if data['layer'] == step+1]

        for prev_node in prev_layer:
            next_node = np.random.choice(next_layer)
            G.add_edge(prev_node,next_node)

        for next_node in next_layer:
            prev_node = np.random.choice(prev_layer)
            G.add_edge(prev_node,next_node)

        for _ in range(2 * num_of_layers):
            while True:
                start_node = np.random.choice([node for node in G.nodes() if node != 'target'])
                end_node = np.random.choice([node for node in G.nodes() if node != 'source' and node != start_node])
                if (start_node,end_node) not in G.edges():
                    G.add_edge(start_node,end_node)
                    break

        for _,_,data in G.edges(data=True):
            data['weight'] = np.random.randint(1,11)
            

    return G


def _random_color_generator():
    color = np.random.randint(0, 256, size=3)/255
    return tuple(color)
    
def draw_flow_network(G):
    if G == None:
        print('Impossible to draw graph: wrong graf podany')
        return
    
    set_of_colors = [_random_color_generator() for _ in range(G.graph['num_of_layers']+2)]

    plot_colors = [set_of_colors[data['layer']] for _,data in G.nodes(data=True)]
    pos = nx.multipartite_layout(G, subset_key="layer")
    
    plt.get_current_fig_manager().full_screen_toggle()
    nx.draw(G,pos,node_color=plot_colors,with_labels=True)
    nx.draw_networkx_edge_labels(G,pos,edge_labels=nx.get_edge_attributes(G,'weight'))
    plt.show()

#####

##### zad 2

def _edmonds_karp_alg(G):
    pass

def ford_fulkerson_alg(G):
    pass