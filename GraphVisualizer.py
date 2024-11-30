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

        nx_graph = nx.Graph()
        
        for node, neighbors in self.graph.adjacency_list.items():
            for neighbor, cost in neighbors:
                nx_graph.add_edge(node, neighbor, weight=cost)
        
        pos = nx.spring_layout(nx_graph) 
        edge_labels = nx.get_edge_attributes(nx_graph, 'weight')

        nx.draw(nx_graph, pos, with_labels=True, node_color="lightblue", node_size=500, font_size=10)
        nx.draw_networkx_edge_labels(nx_graph, pos, edge_labels=edge_labels)
        
        if shortest_path:
            path_edges = list(zip(shortest_path, shortest_path[1:]))
            nx.draw_networkx_edges(nx_graph, pos, edgelist=path_edges, edge_color="red", width=2)

        plt.show()

if __name__ == "__main__":
    delivery_system = DeliverySystem()

    delivery_system.add_route("Warehouse", "CityA", 10)
    delivery_system.add_route("Warehouse", "CityB", 15)
    delivery_system.add_route("CityA", "CityC", 12)
    delivery_system.add_route("CityB", "CityC", 10)
    delivery_system.add_route("CityC", "CityD", 2)
    delivery_system.add_route("CityA", "CityD", 15)

    start_point = "Warehouse"
    end_point = "CityD"
    path, total_cost = delivery_system.get_shortest_route(start_point, end_point)

    print(f"Menor caminho de {start_point} para {end_point}: {' -> '.join(path)}")
    print(f"Custo total: {total_cost}")

    visualizer = GraphVisualizer(delivery_system.graph)
    visualizer.draw_graph(path)
