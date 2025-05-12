##Resolução da questão 1586 : Min Cost to Connect All Points
#Nivel dificil.

from typing import List
import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def manhattan_distance(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        n = len(points)
        visited = set()
        min_heap = [(0, 0)]  
        total_cost = 0

        while len(visited) < n:
            cost, current = heapq.heappop(min_heap)

            if current in visited:
                continue

            total_cost += cost
            visited.add(current)

            for next_point in range(n):
                if next_point not in visited:
                    dist = manhattan_distance(points[current], points[next_point])
                    heapq.heappush(min_heap, (dist, next_point))

        return total_cost