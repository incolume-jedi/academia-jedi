from language_tool_python import LanguageTool

# criar objeto LanguageTool para português do Brasil
tool = LanguageTool('pt-BR')

# texto com erros de ortografia e gramática
texto = 'Eu fiz a prova, porem não tinha estudado o suficiente.'

# obter sugestões de correção
sugestoes = tool.check(texto)

# imprimir sugestões de correção
for sugestao in sugestoes:
    print(sugestao)
