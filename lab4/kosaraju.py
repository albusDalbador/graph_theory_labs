import networkx as nx

def dfs(v, graph, visited, stack):
    visited.add(v)
    for neighbor in graph[v]:
        if neighbor not in visited:
            dfs(neighbor, graph, visited, stack)
    stack.append(v)

def transpose(graph):
    transposed = nx.DiGraph()
    transposed.add_nodes_from(graph.nodes())
    for u, v in graph.edges():
        transposed.add_edge(v, u)
    return transposed

def kosaraju(digraph):
    visited = set()
    stack = []
    for v in digraph.nodes():
        if v not in visited:
            dfs(v, digraph, visited, stack)

    transposed = transpose(digraph)
    visited = set()
    scc = []
    while stack:
        v = stack.pop()
        if v not in visited:
            component = []
            dfs(v, transposed, visited, component)
            scc.append(component)

    return scc