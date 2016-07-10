# Trabalho de busca em largura
# Alunos: Melque Henrique Lemes de Castro




# importa a biblioteca de passagem de argumentos
import sys

# inicia os argumentos na execulcao do programa
inicio = sys.argv[1]
fim = sys.argv[2]

# declaracao do grafo
grafo = {
    'A': ['B', 'E', 'F'],
    'B': ['A', 'C'],
    'C': ['B', 'D'],
    'D': ['C', 'E'],
    'E': ['D', 'A']
}


def bfs(grafo, inicio, fim):
    # cria a fila vazia


    fila = []
    # adiciona um item ao fim da lista
    fila.append([inicio])

    while fila:
        # pega o primeiro caminho da fila
        caminho = fila.pop(0)
        # pega o ultimo no do caminho
        no = caminho[-1]
        # verifica o fim do caminho
        if no == fim:
            return caminho
        # enumera todos os nos adjasentes, controe um novo caminha e coloca na fila
        for adjasente in grafo.get(no, []):
            novo_caminho = list(caminho)
            novo_caminho.append(adjasente)
            fila.append(novo_caminho)


# chama a funcao e printa o caminho
print bfs(grafo, inicio, fim)