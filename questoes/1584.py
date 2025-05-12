##Resolução da questão 1586 : Min Cost to Connect All Points
#Nivel medio.

from typing import List
import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def manhattan_distance(p1, p2): #função auxiliar para calcular a distância de Manhattan entre p1 e p2.
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        n = len(points)
        visited = set()
        min_heap = [(0, 0)]  #Inicia a fila com indice 0 e custo 0
        total_cost = 0

        while len(visited) < n: #contiua enquanto nem todos os nós forem conectados
            cost, current = heapq.heappop(min_heap)

            if current in visited: #ignora o nó caso já  tenha sido conectado
                continue

            total_cost += cost 
            visited.add(current) #marca como já visitado

            for next_point in range(n): #percorre todos os nós para verificar quais não estão conectados
                if next_point not in visited: #caso não foi contectado, prossegue
                    dist = manhattan_distance(points[current], points[next_point]) #calcula a distancia entre nó atual e o proximo
                    heapq.heappush(min_heap, (dist, next_point))

        return total_cost
    
