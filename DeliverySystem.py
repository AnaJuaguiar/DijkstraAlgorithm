import heapq
from typing import Dict, List, Tuple

class DeliverySystem:
    """Representa um sistema de entregas baseado em um grafo ponderado."""
    
    def __init__(self):
        self.routes: Dict[str, List[Tuple[str, int]]] = {}

    def add_route(self, origin: str, destination: str, cost: int) -> None:
        """
        Adiciona uma rota bidirecional entre duas localidades com o custo associado.
        """
        if origin not in self.routes:
            self.routes[origin] = []
        if destination not in self.routes:
            self.routes[destination] = []
        
        self.routes[origin].append((destination, cost))
        self.routes[destination].append((origin, cost))

    def find_shortest_path(self, start: str, end: str) -> Tuple[List[str], int]:
        """
        Encontra o menor caminho entre dois locais usando o algoritmo de Dijkstra.
        Retorna o caminho e o custo total.
        """
        distances = self._initialize_distances(start)
        previous_nodes = {node: None for node in self.routes}
        priority_queue = [(0, start)]

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            # Ignorar distâncias que já foram processadas
            if current_distance > distances[current_node]:
                continue

            for neighbor, cost in self.routes[current_node]:
                self._relax_edge(
                    current_node, neighbor, cost, distances, previous_nodes, priority_queue
                )

        return self._reconstruct_path(previous_nodes, start, end), distances[end]

    def _initialize_distances(self, start: str) -> Dict[str, float]:
        """
        Inicializa todas as distâncias como infinito, exceto o nó inicial, que é zero.
        """
        return {node: float("inf") for node in self.routes} | {start: 0}

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
    path, total_cost = delivery_system.find_shortest_path(start_point, end_point)

    print(f"Menor caminho de {start_point} para {end_point}: {' -> '.join(path)}")
    print(f"Custo total: {total_cost}")
