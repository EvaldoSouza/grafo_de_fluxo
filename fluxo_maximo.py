import networkx as nx

def ford_fulkerson(graph, source, sink):
    # Cria uma cópia do grafo original
    residual_graph = graph.copy()

    # Inicializa o fluxo máximo como 0
    max_flow = 0

    # Enquanto houver um caminho de aumento no grafo residual
    while True:
        # Encontra um caminho de aumento usando o algoritmo de busca em largura
        path = nx.shortest_path(residual_graph, source, sink)

        # Calcula a capacidade residual mínima ao longo do caminho de aumento
        min_capacity = float('inf')
        for u, v in zip(path, path[1:]):
            min_capacity = min(min_capacity, residual_graph[u][v]['capacity'])

        # Atualiza as capacidades residuais das arestas ao longo do caminho de aumento
        for u, v in zip(path, path[1:]):
            residual_graph[u][v]['capacity'] -= min_capacity
            residual_graph[v][u]['capacity'] += min_capacity

        # Atualiza o fluxo máximo
        max_flow += min_capacity

        # Se não houver mais caminhos de aumento, interrompe o loop
        if min_capacity == 0:
            break

    return max_flow

# Exemplo de uso

# Cria um grafo direcionado
graph = nx.DiGraph()

# Adiciona as arestas e suas capacidades
graph.add_edge('A', 'B', capacity=3)
graph.add_edge('A', 'C', capacity=2)
graph.add_edge('B', 'C', capacity=2)
graph.add_edge('B', 'D', capacity=3)
graph.add_edge('C', 'D', capacity=4)
graph.add_edge('C', 'E', capacity=2)
graph.add_edge('D', 'E', capacity=3)

# Calcula o fluxo máximo a partir do nó 'A' até o nó 'E'
source = 'A'
sink = 'E'
max_flow = ford_fulkerson(graph, source, sink)

print("Fluxo máximo:", max_flow)
