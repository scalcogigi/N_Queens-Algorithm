from collections import deque


class ProblemaNDamas:
    def __init__(self, tamanho):
        # Dimensão do tabuleiro.
        # Exemplo: tamanho = 4 representa um tabuleiro 4x4.
        self.tamanho = tamanho

    def posicao_valida(self, estado, nova_coluna):
        """
        Verifica se uma nova dama pode ser colocada na próxima linha.

        O estado é uma tupla em que:
        - o índice representa a linha;
        - o valor representa a coluna da dama.

        Exemplo:
        estado = (1, 3)

        Isso significa:
        - dama na linha 0, coluna 1;
        - dama na linha 1, coluna 3.
        """

        # A próxima dama será colocada depois das damas já existentes.
        nova_linha = len(estado)

        # Percorre todas as damas que já foram posicionadas.
        for linha_existente, coluna_existente in enumerate(estado):

            # Duas damas não podem estar na mesma coluna.
            if coluna_existente == nova_coluna:
                return False

            # Duas damas estão na mesma diagonal quando:
            #
            # diferença entre as linhas
            #              ==
            # diferença entre as colunas
            diferenca_linhas = abs(nova_linha - linha_existente)
            diferenca_colunas = abs(nova_coluna - coluna_existente)

            if diferenca_linhas == diferenca_colunas:
                return False

        # Se não encontrou nenhum conflito, a posição é válida.
        return True

    def sucessores(self, estado):
        """
        Gera todos os estados que podem ser alcançados a partir
        do estado atual.

        Cada sucessor adiciona uma dama válida na próxima linha.
        """

        sucessores = []

        # Testa cada coluna do tabuleiro.
        for coluna in range(self.tamanho):

            # Verifica se a dama pode ser colocada nessa coluna.
            if self.posicao_valida(estado, coluna):

                # Cria um novo estado adicionando a coluna escolhida.
                novo_estado = estado + (coluna,)

                sucessores.append(novo_estado)

        return sucessores

    def objetivo(self, estado):
        """
        O estado é uma solução quando possui uma dama em cada linha.
        """

        return len(estado) == self.tamanho

    def busca_em_largura(self):
        """
        Resolve o problema usando busca em largura — BFS.

        A busca em largura utiliza uma fila:
        - os primeiros estados inseridos são os primeiros processados.
        """

        # O estado inicial não possui nenhuma dama.
        estado_inicial = ()

        # A fila começa apenas com o estado inicial.
        fronteira = deque([estado_inicial])

        # Conta quantos estados foram analisados.
        estados_visitados = 0

        while fronteira:
            # Remove o primeiro estado da fila.
            estado_atual = fronteira.popleft()

            estados_visitados += 1

            # Verifica se o estado atual já é uma solução.
            if self.objetivo(estado_atual):
                return estado_atual, estados_visitados

            # Adiciona todos os sucessores válidos ao final da fila.
            for sucessor in self.sucessores(estado_atual):
                fronteira.append(sucessor)

        # Se a fila acabar, o problema não possui solução.
        return None, estados_visitados

    def mostrar_tabuleiro(self, estado):
        """
        Exibe o tabuleiro no terminal.

        D representa uma dama.
        . representa uma posição vazia.
        """

        for linha in range(self.tamanho):
            linha_tabuleiro = []

            for coluna in range(self.tamanho):
                if estado[linha] == coluna:
                    linha_tabuleiro.append("D")
                else:
                    linha_tabuleiro.append(".")

            print(" ".join(linha_tabuleiro))


def main():
    print("=" * 40)
    print("PROBLEMA DAS N DAMAS")
    print("Algoritmo: Busca em Largura")
    print("=" * 40)

    # Executa o algoritmo para os tamanhos pedidos no enunciado.
    for tamanho in range(4, 9):
        print(f"\nTabuleiro {tamanho}x{tamanho}")

        # Cria o problema para o tamanho atual.
        problema = ProblemaNDamas(tamanho)

        # Executa a busca em largura.
        solucao, estados_visitados = problema.busca_em_largura()

        if solucao is not None:
            print(f"Solução encontrada: {solucao}")
            print(f"Estados visitados: {estados_visitados}\n")

            problema.mostrar_tabuleiro(solucao)
        else:
            print("Não foi encontrada uma solução.")

        print("-" * 40)


if __name__ == "__main__":
    main()