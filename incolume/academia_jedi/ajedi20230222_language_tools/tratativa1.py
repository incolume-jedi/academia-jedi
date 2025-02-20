import logging

# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293
from language_tool_python import LanguageTool


class Exemplos:
    def __init__(self, tool: LanguageTool = None) -> None:
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
