# **📚 Sistema de Entregas com Algoritmo de Dijkstra 📚**

## **📜 Descrição do Projeto**
Este projeto é uma implementação prática do **algoritmo de Dijkstra**, aplicado a um sistema de entregas fictício. O sistema utiliza um grafo para representar cidades e as rotas entre elas, calculando o menor caminho entre dois pontos. Foi desenvolvido como parte da disciplina de **Grafos**.

## **📌 O que é o Algoritmo de Dijkstra?**
O **algoritmo de Dijkstra** é um dos algoritmos mais conhecidos para resolver o problema do menor caminho em um grafo. Ele encontra o menor custo (ou menor distância) entre um nó inicial e os demais nós do grafo, levando em consideração os pesos das arestas. 

### **📢 Funcionamento Básico**
1. Inicializa as distâncias de todos os nós como "infinito", exceto o nó inicial, que tem distância zero.
2. Usa uma fila de prioridade para explorar os nós, sempre escolhendo o nó com a menor distância acumulada.
3. Atualiza as distâncias de seus vizinhos caso encontre um caminho mais curto.
4. Continua até que todos os nós tenham sido visitados ou o destino tenha sido alcançado.

O algoritmo é amplamente utilizado em sistemas de roteamento, redes de computadores e problemas de logística.

---

## **🏗 Arquitetura do Código**

### **1. `Graph.py`**
Define a estrutura do grafo, que é representado como uma lista de adjacência:
- **Funções principais**:
  - `add_edge`: Adiciona uma aresta bidirecional ao grafo.
  - `get_neighbors`: Retorna os vizinhos de um nó.
  - `get_nodes`: Retorna todos os nós do grafo.

---

### **2. `Dijkstra.py`**
Implementa o algoritmo de Dijkstra para encontrar o menor caminho:
- **Funções principais**:
  - `find_shortest_path`: Encontra o menor caminho entre dois nós.
  - `_relax_edge`: Atualiza a distância de um nó vizinho, se um caminho mais curto for encontrado.
  - `_reconstruct_path`: Reconstrói o caminho do destino até o ponto inicial.

---

### **3. `DeliverySystem.py`**
Gerencia a lógica do sistema de entregas, integrando o grafo e o algoritmo de Dijkstra:
- Permite adicionar rotas entre cidades com custos.
- Calcula o menor caminho e o custo total entre dois pontos.

---

### **4. `GraphVisualizer.py`**
Utiliza a biblioteca **NetworkX** e **Matplotlib** para criar uma representação visual do grafo e destacar o menor caminho encontrado.

---

### **5. `main.py`**
O ponto de entrada do projeto. Responsável por:
- Adicionar as cidades e rotas ao sistema.
- Definir os pontos de partida e destino.
- Calcular e exibir o menor caminho e seu custo.
- Visualizar o grafo e o menor caminho destacado.
- Para alterar os pontos onde o caminho deve começar e terminar, selecionar nas linhas 
start_point e 
end_point

---

## **🚩 Requisitos**
- Python 3.8 ou superior
- Dependências:
  - `matplotlib`
  - `networkx`

🌌Para instalar as dependências, use:
```bash
pip install matplotlib networkx
