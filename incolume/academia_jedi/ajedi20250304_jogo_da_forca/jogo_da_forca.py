"""Jogo da forca module."""

import random
from pathlib import Path

from tomli import load

# ruff:noqa:T201
alfabeto = 'abcdefghijklmnopqrstuvxwyz'

chances = 6

palavras_db = Path(__file__).parent / 'palavras.toml'


class Alura:
    """Alura.

    baseado no código disponível em: https://cursos.alura.com.br/forum/topico-codigo-completo-do-jogo-forca-versao-final-122243

    """

    def __init__(self, arq_palavra_secreta: Path | None = None):
        """_summary_

        Args:
            arq_palavra_secreta (Path | None, optional): _description_. Defaults to None.
        """
        self.arq_palavra_secreta = (
            arq_palavra_secreta or Path(__file__).parent / 'palavras.txt'
        )

    def imprime_mensagem_abertura(self):
        """Metodo que imprime mensagem de abertura."""
        print('*********************************')
        print('***Bem vindo ao jogo da Forca!***')
        print('*********************************')

    def carrega_palavra_secreta(self):
        """Carrega palavra secreta do arquivo."""
        palavras = []
        with self.arq_palavra_secreta.open(encoding='utf-8') as arquivo:
            for linha in arquivo:
                linha = linha.strip()
                palavras.append(linha)

        numero = random.randrange(0, len(palavras))
        return palavras[numero].upper()

    def inicializa_letras_acertadas(self, palavra):
        """Inicializa as letras da palavra secreta selecionada."""
        return ['_' for _ in palavra]

    def pede_chute(self) -> str:
        """Pede chute.

        Returns:
            str: resultado
        """
        chute = input('Qual letra? ')
        return chute.strip().upper()

    def marca_chute_correto(
        self,
        chute: str,
        letras_acertadas: list[str],
        palavra_secreta: str,
    ) -> None:
        """Marca a opção correta.

        Args:
            chute (_type_): _description_
            letras_acertadas (_type_): _description_
            palavra_secreta (_type_): _description_
        """
        index = 0
        for letra in palavra_secreta:
            if chute == letra:
                letras_acertadas[index] = letra
            index += 1

    def imprime_mensagem_vencedor(self) -> None:
        """Imprime mensagem vencedor."""
        print('Parabéns, você ganhou!')
        print(r'       ___________      ')
        print(r"      '._==_==_=_.'     ")
        print(r'      .-\\:      /-.    ')
        print(r'     | (|:.     |) |    ')
        print(r"      '-|:.     |-'     ")
        print(r'        \\::.    /      ')
        print(r"         '::. .'        ")
        print(r'           ) (          ')
        print(r"         _.' '._        ")
        print(r"        '-------'       ")

    def imprime_mensagem_perdedor(self, palavra_secreta):
        """Imprime mensagem de perdedor.

        Args:
            palavra_secreta (_type_): _description_
        """
        print('Puxa, você foi enforcado!')
        print(f'A palavra era {palavra_secreta}')
        print(r'    _______________         ')
        print(r'   /               \       ')
        print(r'  /                 \      ')
        print(r'//                   \/\  ')
        print(r'\|   XXXX     XXXX   | /   ')
        print(r' |   XXXX     XXXX   |/     ')
        print(r' |   XXX       XXX   |      ')
        print(r' |                   |      ')
        print(r' \__      XXX      __/     ')
        print(r'   |\     XXX     /|       ')
        print(r'   | |           | |        ')
        print(r'   | I I I I I I I |        ')
        print(r'   |  I I I I I I  |        ')
        print(r'   \_             _/       ')
        print(r'     \_         _/         ')
        print(r'       \_______/           ')

    def desenha_forca(self, erros: int) -> None:
        """Desenha forca."""
        print(r'  _______     ')
        print(r' |/      |    ')

        if erros == 1:
            print(r' |      (_)   ')
            print(r' |            ')
            print(r' |            ')
            print(r' |            ')

        if erros == 2:
            print(r' |      (_)   ')
            print(r' |      \     ')
            print(r' |            ')
            print(r' |            ')

        if erros == 3:
            print(r' |      (_)   ')
            print(r' |      \|    ')
            print(r' |            ')
            print(r' |            ')

        if erros == 4:
            print(r' |      (_)   ')
            print(r' |      \|/   ')
            print(r' |            ')
            print(r' |            ')

        if erros == 5:
            print(r' |      (_)   ')
            print(r' |      \|/   ')
            print(r' |       |    ')
            print(r' |            ')

        if erros == 6:
            print(r' |      (_)   ')
            print(r' |      \|/   ')
            print(r' |       |    ')
            print(r' |      /     ')

        if erros == 7:
            print(r' |      (_)   ')
            print(r' |      \|/   ')
            print(r' |       |    ')
            print(r' |      / \   ')

        print(r' |            ')
        print(r'_|___         ')
        print()

    def jogar(self):
        """Run forca game."""
        self.imprime_mensagem_abertura()

        palavra_secreta = self.carrega_palavra_secreta()

        letras_acertadas = self.inicializa_letras_acertadas(palavra_secreta)

        enforcou = False
        acertou = False
        erros = 0
        letras_faltando = len(letras_acertadas)

        print(letras_acertadas)
        while not acertou and not enforcou:
            chute = self.pede_chute()

            if chute in palavra_secreta:
                self.marca_chute_correto(
                    chute,
                    letras_acertadas,
                    palavra_secreta,
                )
                letras_faltando = str(letras_acertadas.count('_'))
                if letras_faltando == '0':
                    print(
                        f"PARABÉNS!! Você encontrou todas as letras formando a palavra '{palavra_secreta.upper()}'",
                    )
            else:
                erros += 1
                print(letras_acertadas)
                print(f'Ainda faltam acertar {letras_faltando} letras')
                print(f'Você ainda tem {7 - erros} tentativas')
                self.desenha_forca(erros)

            enforcou = erros == 7
            acertou = '_' not in letras_acertadas

            print(letras_acertadas)

        if acertou:
            self.imprime_mensagem_vencedor()
        else:
            self.imprime_mensagem_perdedor(palavra_secreta)

        print('Fim do jogo')


def cabecalho():
    """Header."""
    print('=' * 90)
    print('Jogo da Forca'.center(90))
    print('=' * 90)
    print('Bem vindo! Aperte "ENTER" para começar.')
    print('-' * 90)
    input()
    print('Que comecem os jogos!!!!')


def menu(arquivo_palavras: (str | Path)) -> list[str]:
    """Menu.

    Args:
        arquivo_palavras (str  |  Path): arquivo de base de dados para jogo

    Returns:
        list[str]: palavras
    """
    with Path(arquivo_palavras).open('rb') as file:
        palavras = load(file)
    for opcao in palavras:
        print(f'* {opcao}')
    op = input('Digite uma das opções disponíveis: ')
    return palavras.get(op)


def run():
    """Run it."""
    # cabecalho()
    # print(alfabeto)
    # print(chances)
    # for letra in alfabeto:
    #     print(letra)
    # escolha = input('Digite uma letra do alfabeto: ').lower()
    # print(escolha)
    # print(escolha == "b")
    # with Path('palavras.toml').open('rb') as file:
    #     print(load(file))
    palavras = menu(palavras_db)
    print(palavras)


if __name__ == '__main__':  # pragma: no cover
    # run()
    Alura().jogar()
