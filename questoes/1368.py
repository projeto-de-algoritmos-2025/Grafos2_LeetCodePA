import heapq 

direcoes = {
    1: (0, 1),  
    2: (0, -1), 
    3: (1, 0),   
    4: (-1, 0)   
}

class Solution:
    def minCost(self, grid):
        m, n = len(grid), len(grid[0])  
        custo = [[float('inf')] * n for _ in range(m)]  # Inicializa matriz
        custo[0][0] = 0  # Custo inicial na origem é zero

        fila_prioridade = [(0, 0, 0)]  

        while fila_prioridade:
            custo_atual, x, y = heapq.heappop(fila_prioridade)  # Pega o nó com menor custo

            # Se já visitamos esse nó com custo menor, ignoramos
            if custo_atual > custo[x][y]:
                continue

            # Explora todas as 4 direções possíveis
            for d in range(1, 5):
                dx, dy = direcoes[d]
                nx, ny = x + dx, y + dy

                if 0 <= nx < m and 0 <= ny < n:  # Verifica limites do grid
                    # Se a direção atual é diferente da indicada na célula, adiciona custo 1
                    novo_custo = custo_atual + (1 if grid[x][y] != d else 0)

                    # Se encontramos um caminho mais barato, atualizamos
                    if novo_custo < custo[nx][ny]:
                        custo[nx][ny] = novo_custo
                        heapq.heappush(fila_prioridade, (novo_custo, nx, ny))  # Adiciona novo estado à fila

        return custo[m - 1][n - 1]  # Retorna o menor custo para chegar ao destino (última célula)
