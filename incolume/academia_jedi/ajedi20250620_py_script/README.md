# Acadêmia JEDI

**[Guilda JEDI Incolume](https://discord.gg/eBNamXVtBW) - Grupo Python Incolume**

**JEDI - Junta Especializada de Desenvolvimento e Inovação**
- _[Seja membro da Guilda JEDI Incolume](https://discord.gg/eBNamXVtBW)_

---

## Problema

**Título do problema**

Descrição/apresentação do problema.


## Resultado esperado

O que é esperado na conclusão deste ‘sprint’


## Exemplos

<details>
  <summary>Spoiler?</summary>

  **Passos necessários**:

  1. TDD válido;
  1. Cobertura de testes em 100% do código implementado;
  1. Executar e passar em todos os testes: `$ pytest`;
  1. Executar e passar em todos os linters homologados: `$ task lint`;
  1. Executar e passar no lint ruff: `$ task lint_ruff`;
  1. Executar e passar em todos os linters ativos `$ task lint_all`;

   **Considerar em caso de fatoração**:

    > modo pythônico
    > sem condicionais
    > estruturas performáticas
    > redução de complexidade ciclomática
    > análise assintótica de algoritmos (big O)

</details>

N/A - Exemplos de solução e resposta do problema. Geralmente utilizado para validar os testes do TDD.

## Seguindo as Recomendações da Estrutura de Scripts do Python
Com base nas estruturas e técnicas sobre as quais você aprendeu, aqui estão algumas recomendações para ter em mente ao escrever scripts Python:

- **Esforce-se pela brevidade e clareza**: Os scripts geralmente se beneficiam por serem diretos. Use nomes claros para constantes, funções e variáveis. Embora funções e classes ajudem a organizar seu código, evite aninhamento ou abstração excessivamente profunda se um código linear mais simples dentro do bloco principal for mais fácil de seguir para uma tarefa específica.
- **Alavancar a análise de argumentos para validação de entrada**: Ferramentas como Click são excelentes não apenas para definir argumentos, mas também para validar a entrada do usuário no limite do seu script—por exemplo, usando click.Choice ou type=int. Manipular a validação de entrada aqui geralmente reduz a necessidade de extensão try...except blocos que verificam tipos ou valores profundamente dentro de suas funções lógicas centrais, mantendo-os mais limpos.
- **Abrace dependências independentes**: Para scripts que você pretende compartilhar, PEP 723 é inestimável. Declarar dependências dentro do arquivo de script torna-o reprodutível e muito mais fácil para os outros, e para o uso futuro, para ser executado corretamente usando ferramentas como uv ou pipx.
- **Escolha estruturas de dados com sabedoria**: Selecione a estrutura mais simples que atenda às suas necessidades de clareza e facilidade de manutenção.


Aqui está uma tabela de referência rápida comparando estruturas de dados comuns em um contexto de script. Ele resume quando cada um é mais apropriado com base na complexidade e nos objetivos do seu script:

|Estrutura|	Caso de Uso	|Recomendação|
|---|--|--|
|enum.Enum|	Representando conjuntos fixos de escolhas, estados, modos e entradas de mapeamento.|	Use para maior clareza e digite segurança sobre strings brutas ou inteiros para escolhas predefinidas.|
|collections.namedtuple|	Pacotes de dados simples e imutáveis, valores de retorno de função. Acesso nomeado com baixa sobrecarga.|	Use para registros concisos e fixos onde a imutabilidade é primordial.|
|dataclasses.dataclass|	Registros de dados flexíveis com digitação, menos boilerplate e fácil adição de método.|	Use como um ótimo padrão para a maioria dos dados estruturados. Equilibra recursos, legibilidade |e facilidade.
|class(personalizado)|	Estado complexo, comportamento, padrões de herança. Controle total de OOP.|	Use quando for necessária energia OOP completa. Considere a verbosidade e as necessidades de teste.|

Para o nível de complexidade em seu script, classes de dados e enumerações oferecem a combinação mais adequada de estrutura e simplicidade.


## Referências

 - https://realpython.com/python-script-structure/
 - N/A (Caso haja referências podem ser listadas aqui)


---
Copyright &copy; **incolume.com.br** since 2010
