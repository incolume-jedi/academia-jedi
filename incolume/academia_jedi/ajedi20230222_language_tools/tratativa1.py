from language_tool_python import LanguageTool

# criar objeto LanguageTool para português do Brasil
tool = LanguageTool('pt-BR')

texto = 'O livro que eu comprei são ótimos.'

erros = tool.check(texto)   # verificar erros no texto

# imprimir sugestões de correção para cada erro
for erro in erros:
    print('Erro:', erro.ruleId)
    print('Mensagem:', erro.msg)
    print('Sugestões:', erro.replacements)
    print('Contexto:', erro.context)
    print('Posição:', erro.offset, erro.errorLength)
    print('-----------')
