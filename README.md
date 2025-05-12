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


![Print da Resolução 1368](/assets/img1368.jpg)

### [1584 - Médio](https://leetcode.com/problems/min-cost-to-connect-all-points/description/)

O problema pede para conectar todos os pontos de um plano 2D com o menor custo total possível, onde o custo de conectar dois pontos é a distância de Manhattan entre eles. Para resolver, utilizei o algoritmo de Prim, para construir uma árvore mínima de conexões, conectar todos os pontos sem formar ciclos e com o menor custo. Comecei escolhendo um ponto qualquer, usei uma fila de prioridade (min-heap), conectei os nós um por um, sempre escolhendo o mais próximo com menor custo e calculando a distância dele com todos os pontos ainda não conectados e atualizando a fila com essas novas possibilidades. O algoritmo continua até que todos os pontos estejam conectados, retornando o custo total dessas conexões. 

![Print da Resolução 1584](/assets/1584.jpg)


## Instalação 
**Linguagem**: xxxxxx<br>
**Framework**: (caso exista)<br>
Descreva os pré-requisitos para rodar o seu projeto e os comandos necessários.

## Uso 
Explique como usar seu projeto caso haja algum passo a passo após o comando de execução.

## Outros 
Quaisquer outras informações sobre seu projeto podem ser descritas abaixo.




