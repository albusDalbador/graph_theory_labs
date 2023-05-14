
import numpy as np 


# zad 3.2
def init_dijkstra(G,node):
    d = [np.inf for _ in G.nodes()]
    p = [None for _ in G.nodes()]
    d[node] = 0
    return d,p

def relax_dijkstra(G,u,v,d,p):
    if d[v] > d[u] + G.get_edge_data(u,v)['weight']:
        d[v] = d[u]  + G.get_edge_data(u,v)['weight']
        p[v] = u
    return d,p

def invoke_dijkstra_alg(G,source):
    achieved = []
    d,p = init_dijkstra(G,source)
    while len(achieved) != G.number_of_nodes():
        min_weight = np.min([x for ind,x in enumerate(d) if ind not in achieved])
        u = int([x for x in np.where(d == min_weight)[0] if x not in achieved][0])
        achieved.append(u)

        for v in G.neighbors(u):
            d,p = relax_dijkstra(G,u,v,d,p)

    return d,p
