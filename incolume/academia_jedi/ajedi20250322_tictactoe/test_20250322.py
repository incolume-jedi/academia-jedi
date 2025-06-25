"""Test module."""

# ruff: noqa: PT018, PT011, PLR2004, PT012
from . import Tabuleiro, JogoDaVelha

import pytest
from . import TicTacToe


# Fixture para inicializar a classe TicTacToe
@pytest.fixture
def jogo():
    """Fixture instancia."""
    return TicTacToe()


class TestTicTacToe:
    """Test class."""

    # Testes para exibir_tabuleiro (capturando a saída)
    def test_exibir_tabuleiro_vazio(self, jogo, capsys):
        """Testa se o tabuleiro vazio é exibido corretamente."""
        tabuleiro = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        jogo.exibir_tabuleiro(tabuleiro)
        captured = capsys.readouterr()
        expected_output = '  |   |  \n---------\n  |   |  \n---------\n  |   |  \n---------\n'
        assert captured.out == expected_output

    # Testes para verificar_vitoria
    def test_verificar_vitoria_linha(self, jogo):
        """Testa se a vitória é detectada em uma linha."""
        tabuleiro = [['X', 'X', 'X'], [' ', ' ', ' '], [' ', ' ', ' ']]
        assert jogo.verificar_vitoria(tabuleiro, 'X')

    def test_verificar_vitoria_coluna(self, jogo):
        """Testa se a vitória é detectada em uma coluna."""
        tabuleiro = [['O', ' ', ' '], ['O', ' ', ' '], ['O', ' ', ' ']]
        assert jogo.verificar_vitoria(tabuleiro, 'O')

    def test_verificar_vitoria_diagonal_principal(self, jogo):
        """Testa se a vitória é detectada na diagonal principal."""
        tabuleiro = [['X', ' ', ' '], [' ', 'X', ' '], [' ', ' ', 'X']]
        assert jogo.verificar_vitoria(tabuleiro, 'X')

    def test_verificar_vitoria_diagonal_secundaria(self, jogo):
        """Testa se a vitória é detectada na diagonal secundária."""
        tabuleiro = [[' ', ' ', 'O'], [' ', 'O', ' '], ['O', ' ', ' ']]
        assert jogo.verificar_vitoria(tabuleiro, 'O')

    def test_verificar_vitoria_falha(self, jogo):
        """Testa se a função retorna False quando não há vitória."""
        tabuleiro = [['X', 'O', 'X'], ['O', 'X', 'O'], ['O', 'X', 'O']]
        assert jogo.verificar_vitoria(tabuleiro, 'X') is False

    # Testes para empate
    def test_empate(self, jogo):
        """Testa se o tabuleiro está cheio sem vitória (empate)."""
        tabuleiro = [['X', 'O', 'X'], ['O', 'X', 'O'], ['O', 'X', 'O']]
        jogadas = sum(cell != ' ' for row in tabuleiro for cell in row)
        assert jogadas == 9  # Verifica se todas as células estão preenchidas
        assert (
            jogo.verificar_vitoria(tabuleiro, 'X') is False
        )  # Ninguém venceu

    @pytest.mark.skip
    def test_entrada_invalida(self, monkeypatch, capsys):
        """Simula entrada inválida e verifica a mensagem de erro."""
        monkeypatch.setattr('builtins.input', lambda _: 'invalid')
        jogo = TicTacToe()

        with pytest.raises(ValueError):
            jogo.jogar()
            linha = int(input('Digite a linha (0, 1, 2): '))
            coluna = int(input('Digite a coluna (0, 1, 2): '))
            assert linha.isdigit() and coluna.isdigit()

        captured = capsys.readouterr()
        assert 'Entrada inválida' in captured.out


# Testes para a classe Tabuleiro
class TestTabuleiro:
    """Test class."""

    def setup_method(self):
        """Inicializa um novo tabuleiro antes de cada teste."""
        self.tabuleiro = Tabuleiro()

    def test_exibir_tabuleiro_vazio(self, capsys):
        """Testa se o tabuleiro é exibido corretamente quando vazio."""
        self.tabuleiro.exibir()
        captured = capsys.readouterr()
        expected_output = '  |   |  \n---------\n  |   |  \n---------\n  |   |  \n---------\n'
        assert captured.out == expected_output

    def test_marcar_posicao_valida(self):
        """Testa se uma posição válida pode ser marcada."""
        assert self.tabuleiro.marcar_posicao(0, 0, 'X') is True
        assert self.tabuleiro.tabuleiro[0][0] == 'X'

    def test_marcar_posicao_invalida(self):
        """Testa se uma posição já ocupada não pode ser marcada."""
        self.tabuleiro.marcar_posicao(0, 0, 'X')
        assert self.tabuleiro.marcar_posicao(0, 0, 'O') is False
        assert self.tabuleiro.tabuleiro[0][0] == 'X'

    def test_verificar_vitoria_linha(self):
        """Testa se a vitória é detectada em uma linha."""
        self.tabuleiro.marcar_posicao(0, 0, 'X')
        self.tabuleiro.marcar_posicao(0, 1, 'X')
        self.tabuleiro.marcar_posicao(0, 2, 'X')
        assert self.tabuleiro.verificar_vitoria('X') is True

    def test_verificar_vitoria_coluna(self):
        """Testa se a vitória é detectada em uma coluna."""
        self.tabuleiro.marcar_posicao(0, 0, 'O')
        self.tabuleiro.marcar_posicao(1, 0, 'O')
        self.tabuleiro.marcar_posicao(2, 0, 'O')
        assert self.tabuleiro.verificar_vitoria('O') is True

    def test_verificar_vitoria_diagonal_principal(self):
        """Testa se a vitória é detectada na diagonal principal."""
        self.tabuleiro.marcar_posicao(0, 0, 'X')
        self.tabuleiro.marcar_posicao(1, 1, 'X')
        self.tabuleiro.marcar_posicao(2, 2, 'X')
        assert self.tabuleiro.verificar_vitoria('X') is True

    def test_verificar_vitoria_diagonal_secundaria(self):
        """Testa se a vitória é detectada na diagonal secundária."""
        self.tabuleiro.marcar_posicao(0, 2, 'O')
        self.tabuleiro.marcar_posicao(1, 1, 'O')
        self.tabuleiro.marcar_posicao(2, 0, 'O')
        assert self.tabuleiro.verificar_vitoria('O') is True

    def test_verificar_empate(self):
        """Testa se o tabuleiro está cheio (empate)."""
        jogadas = [
            (0, 0, 'X'),
            (0, 1, 'O'),
            (0, 2, 'X'),
            (1, 0, 'O'),
            (1, 1, 'X'),
            (1, 2, 'O'),
            (2, 0, 'X'),
            (2, 1, 'O'),
            (2, 2, 'X'),
        ]
        for linha, coluna, jogador in jogadas:
            self.tabuleiro.marcar_posicao(linha, coluna, jogador)
        assert self.tabuleiro.esta_cheio() is True


# Testes para a classe JogoDaVelha
class TestJogoDaVelha:
    """Test class."""

    def setup_method(self):
        """Inicializa um novo jogo antes de cada teste."""
        self.jogo = JogoDaVelha()

    def test_alternar_jogador(self):
        """Testa se o jogador alterna corretamente."""
        assert self.jogo.jogador_atual == 'X'
        self.jogo.alternar_jogador()
        assert self.jogo.jogador_atual == 'O'
        self.jogo.alternar_jogador()
        assert self.jogo.jogador_atual == 'X'
