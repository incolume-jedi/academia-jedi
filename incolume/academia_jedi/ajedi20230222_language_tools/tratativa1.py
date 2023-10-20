import logging

from language_tool_python import LanguageTool


class Exemplos:
    def __init__(self, tool: LanguageTool = None):
        # criar objeto LanguageTool para português do Brasil
        self.tool = tool or LanguageTool('pt-BR')

    def ex1(self, texto: str = ''):
        """"""
        logging.debug(texto)

        erros = self.tool.check(texto)  # verificar erros no texto
        logging.debug(erros)

        # imprimir sugestões de correção para cada erro
        for erro in erros:
            print('Erro:', erro.ruleId)
            print('Mensagem:', erro.msg)
            print('Sugestões:', erro.replacements)
            print('Contexto:', erro.context)
            print('Posição:', erro.offset, erro.errorLength)
            print('-----------')

    def ex2(self, texto: str = ''):
        """"""
        # texto com erros de ortografia e gramática
        texto = (
            texto or 'Eu fiz a prova, porem não tinha estudado o suficiente.'
        )
        logging.debug(texto)

        # obter sugestões de correção
        sugestoes = self.tool.check(texto)
        logging.debug(sugestoes)

        # imprimir sugestões de correção
        for sugestao in sugestoes:
            print(sugestao)


def run():
    # criar objeto LanguageTool para português do Brasil
    tool = LanguageTool('pt-BR')
    logging.debug(tool)
    exemplo = Exemplos(tool)

    textos = [
        'O livro que eu comprei são ótimos.',
        'Eu fiz a prova, porem não tinha estudado o suficiente.',
    ]
    logging.debug(textos)
    print('---  ex1 ---')
    exemplo.ex1(texto=textos[0])
    print('---  ex2 ---')
    exemplo.ex2(texto=textos[1])


if __name__ == '__main__':  # pragma: no cover
    run()
