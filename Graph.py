from typing import Dict, List, Tuple

class Graph:
    """Gerencia o grafo com os nós e arestas."""
    
    def __init__(self):
        self.adjacency_list: Dict[str, List[Tuple[str, int]]] = {}

    def add_edge(self, origin: str, destination: str, cost: int) -> None:
        """
        Adiciona uma aresta bidirecional entre dois nós no grafo.
        """
        if origin not in self.adjacency_list:
            self.adjacency_list[origin] = []
        if destination not in self.adjacency_list:
            self.adjacency_list[destination] = []
        
        self.adjacency_list[origin].append((destination, cost))
        self.adjacency_list[destination].append((origin, cost))

    def get_neighbors(self, node: str) -> List[Tuple[str, int]]:
        """
        Retorna os vizinhos de um nó e os custos associados.
        """
        return self.adjacency_list.get(node, [])

    def get_nodes(self) -> List[str]:
        """
        Retorna todos os nós do grafo.
        """
        return list(self.adjacency_list.keys())
