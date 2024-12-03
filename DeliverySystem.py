from typing import List, Tuple

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
