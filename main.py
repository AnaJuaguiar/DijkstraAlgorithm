


import DeliverySystem
import GraphVisualizer


if __name__ == "__main__":
    delivery_system = DeliverySystem.DeliverySystem()

    # Adiciona cidades e rotas
    delivery_system.add_route("Warehouse", "CityA", 10)
    delivery_system.add_route("Warehouse", "CityB", 15)
    delivery_system.add_route("CityA", "CityC", 12)
    delivery_system.add_route("CityB", "CityC", 10)
    delivery_system.add_route("CityC", "CityD", 2)
    delivery_system.add_route("CityA", "CityD", 15)
    delivery_system.add_route("CityD", "CityE", 5)
    delivery_system.add_route("CityE", "CityF", 7)
    delivery_system.add_route("CityB", "CityF", 20)
    delivery_system.add_route("CityA", "CityF", 25)

    # Define pontos de partida e destino
    start_point = "Warehouse"
    end_point = "CityC"

    try:
        # Calcula o menor caminho
        path, total_cost = delivery_system.get_shortest_route(start_point, end_point)

        # Exibe os resultados
        print(f"Menor caminho de {start_point} para {end_point}: {' -> '.join(path)}")
        print(f"Custo total: {total_cost}")

        # Visualiza o grafo
        visualizer = GraphVisualizer.GraphVisualizer(delivery_system.graph)
        visualizer.draw_graph(path)
    except ValueError as e:
        print(e)
