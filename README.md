# Grafos2_LeetCodePA


**Número da Lista**: 2<br>
**Conteúdo da Disciplina**: Grafos 2<br>

## Alunos
|Matrícula | Aluno |
| -- | -- |
| 20/2015868 |  Alexandre Lema Xavier Júnior |
| 21/1039671  |  Pedro Lopes da Cunha |

## Sobre 
Resolução de questões do LeetCode (2 difíceis e uma média) pelos integrantes do grupo com o objetivo de demonstrar o conhecimento adquirido nesse módulo (Grafos 2) da disciplina.

## Screenshots

### [1368 - Difícil](https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/description/) 

Implementei o algoritmo de Dijkstra para encontrar o caminho de menor custo em um grafo direcionado e ponderado, modelado a partir de uma grade 2D onde cada célula representa um nó. Cada aresta conecta uma célula à sua vizinha de acordo com a direção indicada, com custo 0 se a direção for seguida corretamente ou custo 1 caso seja necessário alterar a seta. Utilize uma fila de prioridade para explorar primeiro os caminhos de menor custo, atualizando os menores valores de custo para alcançar cada célula. Ao final, retornei o menor custo necessário para alcançar a célula destino no canto inferior direito da grade.

https://github.com/user-attachments/assets/89318cdf-0bde-4c27-a729-b20abc90f4cb

![Print da Resolução 1368](/assets/img1368.jpg)

### [1584 - Médio](https://leetcode.com/problems/min-cost-to-connect-all-points/description/)

O problema pede para conectar todos os pontos de um plano 2D com o menor custo total possível, onde o custo de conectar dois pontos é a distância de Manhattan entre eles. Para resolver, utilizei o algoritmo de Prim, para construir uma árvore mínima de conexões, conectar todos os pontos sem formar ciclos e com o menor custo. Comecei escolhendo um ponto qualquer, usei uma fila de prioridade (min-heap), conectei os nós um por um, sempre escolhendo o mais próximo com menor custo e calculando a distância dele com todos os pontos ainda não conectados e atualizando a fila com essas novas possibilidades. O algoritmo continua até que todos os pontos estejam conectados, retornando o custo total dessas conexões. 


https://github.com/user-attachments/assets/298600a7-7e2e-453f-8b46-0f8db534cdfa

![Print da Resolução 1584](/assets/1584.jpg)

## [2290 - Dificil](https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/)

O problema consiste em encontrar o menor número de obstáculos que precisam ser removidos para que seja possível se mover da célula (0, 0) até (m-1, n-1) em uma grade 2D onde: 0 representa uma célula livre (pode andar sem custo), 1 representa um obstáculo (precisa ser "removido" com custo 1 para passar). Para resolver esse problema, foi utilizado o algoritmo de Dijkstra, ideal para encontrar o caminho mais curto em um grafo ponderado com valores não negativos. Cada célula da grade é convertida em um nó de um grafo, conectado aos vizinhos da direita e de baixo, o valor da célula (0 ou 1) representa o custo para entrar nela (livre ou precisa remover obstáculo), o algoritmo percorre os caminhos com menor custo acumulado primeiro, somando os obstáculos removidos, ao chegar na última célula, o custo acumulado representa o número mínimo de obstáculos a remover.

https://github.com/user-attachments/assets/c49d6011-63b8-4b29-8b7d-2087f1c2cbd2

![Print da Resolução 2290](/assets/2290.jpg)

## Instalação 
**Linguagem**: Python<br>




