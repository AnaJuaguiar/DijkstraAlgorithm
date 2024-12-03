import heapq
from typing import Dict, List, Tuple
from Graph import Graph

class Dijkstra:
    """Implementa o algoritmo de Dijkstra para encontrar o menor caminho."""
    
    def find_shortest_path(self, graph: Graph, start: str, end: str) -> Tuple[List[str], int]:
        """
        Encontra o menor caminho entre dois nós no grafo.
        Retorna o caminho e o custo total.
        """
        distances = self._initialize_distances(graph, start)
        previous_nodes = {node: None for node in graph.get_nodes()}
        priority_queue = [(0, start)]

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            if current_distance > distances[current_node]:
                continue

            for neighbor, cost in graph.get_neighbors(current_node):
                self._relax_edge(
                    current_node, neighbor, cost, distances, previous_nodes, priority_queue
                )

        if distances[end] == float("inf"):
            raise ValueError(f"Não há caminho disponível entre {start} e {end}.")

        return self._reconstruct_path(previous_nodes, start, end), distances[end]

    def _initialize_distances(self, graph: Graph, start: str) -> Dict[str, float]:
        """
        Inicializa as distâncias como infinito, exceto o nó inicial, que é zero.
        """
        return {node: float("inf") for node in graph.get_nodes()} | {start: 0}

    def _relax_edge(
        self, 
        current_node: str, 
        neighbor: str, 
        cost: int, 
        distances: Dict[str, float], 
        previous_nodes: Dict[str, str], 
        priority_queue: List[Tuple[int, str]]
    ) -> None:
        """
        Relaxa uma aresta, atualizando a distância e o nó anterior se um caminho mais curto for encontrado.
        """
        new_distance = distances[current_node] + cost
        if new_distance < distances[neighbor]:
            distances[neighbor] = new_distance
            previous_nodes[neighbor] = current_node
            heapq.heappush(priority_queue, (new_distance, neighbor))

    def _reconstruct_path(self, previous_nodes: Dict[str, str], start: str, end: str) -> List[str]:
        """
        Reconstrói o menor caminho a partir do nó final para o inicial.
        """
        path = []
        current = end
        while current:
            path.append(current)
            current = previous_nodes[current]
        return path[::-1]  # Inverte o caminho
