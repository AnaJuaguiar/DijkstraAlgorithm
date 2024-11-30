from typing import List
import matplotlib.pyplot as plt
import networkx as nx
from networkx import Graph

from DeliverySystem import DeliverySystem

class GraphVisualizer:
    """Responsável por criar representações gráficas de um grafo."""
    def __init__(self, graph: Graph):
        self.graph = graph

    def draw_graph(self, shortest_path: List[str] = None) -> None:
        """
        Desenha o grafo completo e destaca o menor caminho, se fornecido.
        """
        # Criar o grafo com NetworkX
        nx_graph = nx.Graph()
        
        # Adicionar arestas
        for node, neighbors in self.graph.adjacency_list.items():
            for neighbor, cost in neighbors:
                nx_graph.add_edge(node, neighbor, weight=cost)
        
        # Configurações para pesos das arestas
        pos = nx.spring_layout(nx_graph)  # Layout do grafo
        edge_labels = nx.get_edge_attributes(nx_graph, 'weight')
        
        # Desenhar o grafo completo
        nx.draw(nx_graph, pos, with_labels=True, node_color="lightblue", node_size=500, font_size=10)
        nx.draw_networkx_edge_labels(nx_graph, pos, edge_labels=edge_labels)
        
        # Destacar o menor caminho, se fornecido
        if shortest_path:
            path_edges = list(zip(shortest_path, shortest_path[1:]))
            nx.draw_networkx_edges(nx_graph, pos, edgelist=path_edges, edge_color="red", width=2)

        # Exibir o grafo
        plt.show()


# Exemplo de uso
if __name__ == "__main__":
    delivery_system = DeliverySystem()

    # Adiciona rotas no sistema
    delivery_system.add_route("Warehouse", "CityA", 10)
    delivery_system.add_route("Warehouse", "CityB", 15)
    delivery_system.add_route("CityA", "CityC", 12)
    delivery_system.add_route("CityB", "CityC", 10)
    delivery_system.add_route("CityC", "CityD", 2)
    delivery_system.add_route("CityA", "CityD", 15)

    # Calcula o menor caminho do armazém até CityD
    start_point = "Warehouse"
    end_point = "CityD"
    path, total_cost = delivery_system.get_shortest_route(start_point, end_point)

    print(f"Menor caminho de {start_point} para {end_point}: {' -> '.join(path)}")
    print(f"Custo total: {total_cost}")

    # Visualizar o grafo
    visualizer = GraphVisualizer(delivery_system.graph)
    visualizer.draw_graph(path)
