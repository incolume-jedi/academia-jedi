"""Module."""

# ruff: noqa: T201, C901, FBT003, E501, S311, PLR2004, PLR0912, SIM103

import random


class Tabuleiro:
    """Classe que representa o tabuleiro do jogo."""

    def __init__(self):
        """Init."""
        self.tabuleiro = [[' ' for _ in range(3)] for _ in range(3)]

    def exibir(self):
        """Exibe o estado atual do tabuleiro."""
        for linha in self.tabuleiro:
            print(' | '.join(linha))
            print('-' * 9)

    def marcar_posicao(self, linha, coluna, jogador):
        """Marca uma posição no tabuleiro para o jogador."""
        if self.tabuleiro[linha][coluna] == ' ':
            self.tabuleiro[linha][coluna] = jogador
            return True
        return False

    def verificar_vitoria(self, jogador):
        """Verifica se o jogador venceu."""
        # Verifica linhas e colunas
        for i in range(3):
            if all(self.tabuleiro[i][j] == jogador for j in range(3)) or all(
                self.tabuleiro[j][i] == jogador for j in range(3)
            ):
                return True

        # Verifica diagonais
        if all(self.tabuleiro[i][i] == jogador for i in range(3)) or all(
            self.tabuleiro[i][2 - i] == jogador for i in range(3)
        ):
            return True

        return False

    def esta_cheio(self):
        """Verifica se o tabuleiro está cheio (empate)."""
        return all(
            self.tabuleiro[i][j] != ' ' for i in range(3) for j in range(3)
        )


class JogoDaVelha:
    """Classe principal que controla o jogo."""

    def __init__(self, tabuleiro: Tabuleiro | None = None):
        """Init class.

        Inicializa o tabuleiro e define o jogador atual.

        Args:
            tabuleiro (Tabuleiro | None, optional): _description_. Defaults to None.
        """
        self.tabuleiro = tabuleiro or Tabuleiro()
        self.jogador_atual = 'X'

    def alternar_jogador(self):
        """Altera o jogador atual."""
        self.jogador_atual = 'O' if self.jogador_atual == 'X' else 'X'

    def jogar(self):
        """Executa o jogo."""
        print('Bem-vindo ao Jogo da Velha!')
        self.tabuleiro.exibir()

        while True:
            print(f'Vez do jogador {self.jogador_atual}')
            try:
                linha = int(input('Digite a linha (0, 1, 2): '))
                coluna = int(input('Digite a coluna (0, 1, 2): '))

                # Tenta marcar a posição
                if not self.tabuleiro.marcar_posicao(
                    linha,
                    coluna,
                    self.jogador_atual,
                ):
                    print('Essa posição já está ocupada. Tente novamente.')
                    continue

                # Exibe o tabuleiro após a jogada
                self.tabuleiro.exibir()

                # Verifica vitória
                if self.tabuleiro.verificar_vitoria(self.jogador_atual):
                    print(f'Parabéns! O jogador {self.jogador_atual} venceu!')
                    break

                # Verifica empate
                if self.tabuleiro.esta_cheio():
                    print('Empate! Ninguém venceu.')
                    break

                # Alterna para o próximo jogador
                self.alternar_jogador()

            except (ValueError, IndexError):
                print(
                    'Entrada inválida. Certifique-se de digitar números entre 0 e 2.',
                )
                continue


class TicTacToe:
    """TicTacToe class."""

    def exibir_tabuleiro(self, tabuleiro):
        """Exibe o tabuleiro atual na tela."""
        for linha in tabuleiro:
            print(' | '.join(linha))
            print('-' * 9)

    def verificar_vitoria(self, tabuleiro, jogador):
        """Verifica se o jogador atual venceu."""
        # Verifica linhas, colunas e diagonais
        for i in range(3):
            if all(tabuleiro[i][j] == jogador for j in range(3)):  # Linha
                return True
            if all(tabuleiro[j][i] == jogador for j in range(3)):  # Coluna
                return True

        # Diagonal principal
        if all(tabuleiro[i][i] == jogador for i in range(3)):
            return True

        # Diagonal secundária
        if all(tabuleiro[i][2 - i] == jogador for i in range(3)):
            return True

        return False

    def jogar(
        self,
    ):
        """Função principal para jogar o jogo."""
        # Inicializa o tabuleiro vazio
        tabuleiro = [[' ' for _ in range(3)] for _ in range(3)]
        jogador_atual = 'X'

        print('Bem-vindo ao Jogo da Velha!')
        self.exibir_tabuleiro(tabuleiro)

        jogadas = 0
        while jogadas < 9:
            # Solicita a jogada ao jogador atual
            print(f'Vez do jogador {jogador_atual}')
            try:
                linha = int(input('Digite a linha (0, 1, 2): '))
                coluna = int(input('Digite a coluna (0, 1, 2): '))

                # Verifica se a posição está disponível
                if tabuleiro[linha][coluna] != ' ':
                    print('Essa posição já está ocupada. Tente novamente.')
                    continue

                # Marca a jogada no tabuleiro
                tabuleiro[linha][coluna] = jogador_atual
                self.exibir_tabuleiro(tabuleiro)
                jogadas += 1

                # Verifica se o jogador venceu
                if self.verificar_vitoria(tabuleiro, jogador_atual):
                    print(f'Parabéns! O jogador {jogador_atual} venceu!')
                    break

                # Alterna para o próximo jogador
                jogador_atual = 'O' if jogador_atual == 'X' else 'X'

            except (ValueError, IndexError):
                print(
                    'Entrada inválida. Certifique-se de digitar números entre 0 e 2.',
                )
                continue

        if jogadas == 9:
            print('Empate! Ninguém venceu.')


class Tictactoe:
    """Classe principal do Jogo da Velha."""

    def __init__(self):
        """Init class."""
        self.tabuleiro = [[' ' for _ in range(3)] for _ in range(3)]
        self.jogador_atual = 'X'
        self.placar = {'Jogador': 0, 'Computador': 0}

    def exibir_tabuleiro(self):
        """Exibe o tabuleiro atual."""
        for linha in self.tabuleiro:
            print(' | '.join(linha))
            print('-' * 9)

    def verificar_vitoria(self, jogador):
        """Verifica se o jogador venceu."""
        # Verifica linhas, colunas e diagonais
        for i in range(3):
            if all(self.tabuleiro[i][j] == jogador for j in range(3)) or all(
                self.tabuleiro[j][i] == jogador for j in range(3)
            ):
                return True
        if all(self.tabuleiro[i][i] == jogador for i in range(3)) or all(
            self.tabuleiro[i][2 - i] == jogador for i in range(3)
        ):
            return True
        return False

    def esta_cheio(self):
        """Verifica se o tabuleiro está cheio (empate)."""
        return all(
            self.tabuleiro[i][j] != ' ' for i in range(3) for j in range(3)
        )

    def marcar_posicao(self, linha, coluna, jogador):
        """Marca uma posição no tabuleiro."""
        if self.tabuleiro[linha][coluna] == ' ':
            self.tabuleiro[linha][coluna] = jogador
            return True
        return False

    def jogada_computador_facil(self):
        """Nível fácil: Jogada aleatória."""
        while True:
            linha, coluna = random.randint(0, 2), random.randint(0, 2)
            if self.marcar_posicao(linha, coluna, 'O'):
                break

    def jogada_computador_medio(self):
        """Nível médio: Tenta bloquear o jogador ou faz jogadas estratégicas simples."""
        # Primeiro, tenta ganhar se possível
        for i in range(3):
            for j in range(3):
                if self.tabuleiro[i][j] == ' ':
                    self.tabuleiro[i][j] = 'O'
                    if self.verificar_vitoria('O'):
                        return
                    self.tabuleiro[i][j] = ' '  # Desfaz a jogada

        # Depois, tenta bloquear o jogador
        for i in range(3):
            for j in range(3):
                if self.tabuleiro[i][j] == ' ':
                    self.tabuleiro[i][j] = 'X'
                    if self.verificar_vitoria('X'):
                        self.tabuleiro[i][j] = 'O'
                        return
                    self.tabuleiro[i][j] = ' '  # Desfaz a jogada

        # Se não houver movimento óbvio, faz uma jogada aleatória
        self.jogada_computador_facil()

    def minimax(self, tabuleiro, profundidade, maximizando):
        """Algoritmo Minimax para o nível impossível."""
        if self.verificar_vitoria('O'):
            return 10 - profundidade
        if self.verificar_vitoria('X'):
            return profundidade - 10
        if self.esta_cheio():
            return 0

        if maximizando:
            melhor_valor = float('-inf')
            for i in range(3):
                for j in range(3):
                    if tabuleiro[i][j] == ' ':
                        tabuleiro[i][j] = 'O'
                        valor = self.minimax(
                            tabuleiro,
                            profundidade + 1,
                            False,
                        )
                        tabuleiro[i][j] = ' '
                        melhor_valor = max(melhor_valor, valor)
            return melhor_valor
        melhor_valor = float('inf')
        for i in range(3):
            for j in range(3):
                if tabuleiro[i][j] == ' ':
                    tabuleiro[i][j] = 'X'
                    valor = self.minimax(tabuleiro, profundidade + 1, True)
                    tabuleiro[i][j] = ' '
                    melhor_valor = min(melhor_valor, valor)
        return melhor_valor

    def jogada_computador_impossivel(self):
        """Nível impossível: Usa o algoritmo Minimax."""
        melhor_valor = float('-inf')
        melhor_jogada = (-1, -1)

        for i in range(3):
            for j in range(3):
                if self.tabuleiro[i][j] == ' ':
                    self.tabuleiro[i][j] = 'O'
                    valor = self.minimax(self.tabuleiro, 0, False)
                    self.tabuleiro[i][j] = ' '
                    if valor > melhor_valor:
                        melhor_valor = valor
                        melhor_jogada = (i, j)

        linha, coluna = melhor_jogada
        self.marcar_posicao(linha, coluna, 'O')

    def jogar(self):
        """Executa o jogo."""
        print('Bem-vindo ao Jogo da Velha!')
        nivel = input(
            'Escolha o nível do computador (1-Fácil, 2-Médio, 3-Impossível): ',
        )
        while nivel not in ['1', '2', '3']:
            nivel = input(
                'Opção inválida. Escolha o nível'
                ' (1-Fácil, 2-Médio, 3-Impossível): ',
            )

        while True:
            self.tabuleiro = [[' ' for _ in range(3)] for _ in range(3)]
            print('\nNova partida:')
            self.exibir_tabuleiro()

            while True:
                # Jogada do jogador humano
                print(f'Vez do jogador {self.jogador_atual}')
                try:
                    linha = int(input('Digite a linha (0, 1, 2): '))
                    coluna = int(input('Digite a coluna (0, 1, 2): '))
                    if not self.marcar_posicao(linha, coluna, 'X'):
                        print('Posição ocupada. Tente novamente.')
                        continue
                except (ValueError, IndexError):
                    print(
                        'Entrada inválida. Certifique-se'
                        ' de digitar números entre 0 e 2.',
                    )
                    continue

                self.exibir_tabuleiro()
                if self.verificar_vitoria('X'):
                    print('Parabéns! Você venceu!')
                    self.placar['Jogador'] += 1
                    break

                if self.esta_cheio():
                    print('Empate!')
                    break

                # Jogada do computador
                print('Vez do computador...')
                if nivel == '1':
                    self.jogada_computador_facil()
                elif nivel == '2':
                    self.jogada_computador_medio()
                elif nivel == '3':
                    self.jogada_computador_impossivel()

                self.exibir_tabuleiro()
                if self.verificar_vitoria('O'):
                    print('O computador venceu!')
                    self.placar['Computador'] += 1
                    break

                if self.esta_cheio():
                    print('Empate!')
                    break

            print(
                f'\nPlacar: Jogador {self.placar["Jogador"]}'
                f' x {self.placar["Computador"]} Computador',
            )
            continuar = input('Deseja jogar novamente? (s/n): ').lower()
            if continuar != 's':
                print('Obrigado por jogar!')
                break


# Executa o jogo
if __name__ == '__main__':
    TicTacToe().jogar()

    jogo = JogoDaVelha()
    jogo.jogar()

    jogo = Tictactoe()
    jogo.jogar()
