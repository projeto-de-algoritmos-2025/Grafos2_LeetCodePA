import collections
import heapq
from typing import List

class Solution:
  def minimumObstacles(self, grid: List[List[int]]) -> int:
    g = collections.defaultdict(list)

    lines = len(grid)
    colums = len(grid[0])

    # Vetor que armazena o valor de cada célula (0 = livre, 1 = obstáculo), representado em forma linear
    walls = [0] * lines * colums
        
    # Construção do grafo a partir da grade
    for line_num in range(lines):
      for col_num in range(colums):
        node_number = col_num + colums * line_num  # Índice linear da célula atual
        if (col_num + 1) in range(colums):
          neighbor_number = (col_num + 1) + colums * line_num  # Vizinho à direita
          g[node_number].append(neighbor_number)
          g[neighbor_number].append(node_number)
        if (line_num + 1) in range(len(grid)):
          neighbor_number = col_num + colums * (line_num + 1)  # Vizinho abaixo
          g[node_number].append(neighbor_number)
          g[neighbor_number].append(node_number)
        walls[node_number] = grid[line_num][col_num]  # Armazena o valor da célula atual (0 ou 1)
    
    # Algoritmo de Dijkstra para encontrar o caminho com menor número de obstáculos
    path_array = [0] * lines * colums
    last_node = (lines * colums) - 1  # Índice da célula final (canto inferior direito)
    heap = [(walls[0], 0, 0)]  # (obstáculos até o momento, índice atual, índice anterior)
    visited = set()

    while heap:
      is_wall, current, prev = heapq.heappop(heap)
      if current not in visited:
        visited.add(current)
        path_array[current] = is_wall  # Armazena o custo (número de obstáculos) para chegar a este nó
        if current == last_node:
          break  # Encerra se chegou ao destino
        for neighbor in g[current]:
          if neighbor not in visited:
            # Soma o valor do vizinho (0 ou 1) ao custo atual e insere na fila
            heapq.heappush(heap, (walls[neighbor] + is_wall, neighbor, current))
    
    return path_array[last_node]  # Retorna o menor número de obstáculos a serem removidos
          
print(Solution.minimumObstacles(Solution, [[0,1,1],[1,1,0],[1,1,0]]))
