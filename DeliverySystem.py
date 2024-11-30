from typing import Dict, List, Tuple
from Dijkstra import Dijkstra
from Graph import Graph


class DeliverySystem:
    """Gerencia o sistema de entregas, integrando o grafo e o algoritmo."""
    def __init__(self):
        self.graph = Graph()
        self.algorithm = Dijkstra()

    def add_route(self, origin: str, destination: str, cost: int) -> None:
        """
        Adiciona uma rota ao grafo.
        """
        self.graph.add_edge(origin, destination, cost)

    def get_shortest_route(self, start: str, end: str) -> Tuple[List[str], int]:
        """
        Calcula o menor caminho entre dois pontos usando o algoritmo de Dijkstra.
        """
        return self.algorithm.find_shortest_path(self.graph, start, end)


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
