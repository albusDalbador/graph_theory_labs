import sys

def prim_algorithm(graph):
    
    mst_vertices = []
    min_edge_weights = {}
    parents = {}
    
    for i in range(len(graph)):
        min_edge_weights[i] = float('inf')
        parents[i] = None
    
    min_edge_weights[0] = 0
    
    while len(mst_vertices) < len(graph):
        min_weight_vertex = None
        for i in range(len(graph)):
            if i not in mst_vertices:
                if min_weight_vertex is None or min_edge_weights[i] < min_edge_weights[min_weight_vertex]:
                    min_weight_vertex = i
        
        mst_vertices.append(min_weight_vertex)
        
        for i in range(len(graph)):
            if graph[min_weight_vertex][i] != 0 and i not in mst_vertices:
                if graph[min_weight_vertex][i] < min_edge_weights[i]:
                    min_edge_weights[i] = graph[min_weight_vertex][i]
                    parents[i] = min_weight_vertex
    

    mst_edges = []
    total_weight = 0
    
    for i in range(1, len(graph)):
        mst_edges.append((parents[i], i))
        total_weight += graph[parents[i]][i]
    
    return mst_edges, total_weight