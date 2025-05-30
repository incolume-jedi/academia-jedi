# Acadêmia JEDI

**[Guilda JEDI Incolume](https://discord.gg/eBNamXVtBW) - Grupo Python Incolume**

**JEDI - Junta Especializada de Desenvolvimento e Inovação**
- _[Seja membro da Guilda JEDI Incolume](https://discord.gg/eBNamXVtBW)_

---

## Problema

**Converter imagens em texto através de agente de IA**

### Primeira versão prompt

```markdown
São paginas contém um ou mais atos normativos do governo brasileiro do século 18. Preciso que você acesse o texto identifique o encode, e mantenha o texto em português arcaico. Em cada página há um título e o número de página, remova-os.

Você como linguista especialista em língua portuguesa do século 18, me entregará um arquivo com o texto revisado e corrigido sem alteração do original.
```

### 2ª Versão de prompt

```bash
    Você é um especialista em documentos históricos brasileiros do século XIX, com domínio do português arcaico e conhecimento em paleografia. Analise os textos fornecidos e extraia cada ato normativo (cartas régias, decretos, alvarás) no seguinte formato JSON:

    [
      {
        "epigrafe": "[TIPO DO DOCUMENTO] [DATA POR EXTENSO]",
        "tipo": "[TIPO DO DOCUMENTO]",
        "data": "[DATA NO FORMATO ISO YYYY-MM-DD]",
        "ementa": "[RESUMO CONCISO DO DOCUMENTO EM 1 FRASE]",
        "content": "[TEXTO COMPLETO DO DOCUMENTO, MANTENDO O PORTUGUÊS ARCAICO ORIGINAL]",
        "data_assinatura": "[LOCAL E DATA DE ASSINATURA POR EXTENSO]",
        "assinatura": "[TEXTO COMPLETO DA ASSINATURA/RUBRICA]"
      }
    ]

    Regras estritas:
    1. Mantenha rigorosamente o texto original em português arcaico
    2. Converta datas para formato ISO (1808-02-23) quando possível
    3. Para a ementa, extraia a essência do documento em linguagem contemporânea, mas mantendo termos jurídicos históricos
    4. Remova cabeçalhos, números de página e formatações originais
    5. Trate cada documento como um objeto JSON separado no array
    6. Preserve todas as particularidades ortográficas originais (como "commercio", "sciencia", etc.)
    7. Para documentos longos com múltiplas páginas, una o conteúdo mantendo a integridade textual
    8. content deverá conter texto do conteudo completo do ato.

    Exemplo de saída esperada:
    ```json
    [
      {
        "epigrafe": "Decreto de 23 de fevereiro de 1808",
        "tipo": "DECRETO",
        "data": "1808-02-23",
        "ementa": "Criação de cadeira de Ciência Econômica no Rio de Janeiro",
        "content": "Sendo absolutamente necessario o estudo da Sciencia Economica na presente conjunctura em que o Brazil oferece a melhor occasião de se pôr em pratica muitos dos seus princípios, para que os meus vassalios sendo melhor instruídos nele, me possam servir com mais vantagem: e por me constar que José da Silva Lisboa, Deputado e Secretario da Mesa da Inspecção da Agricultura e Commercio da Cidade da Bahia, tem dado todas as provas de ser muito hábil para o ensino daquella sciencia sem a qual se caminha às cegas e com passos muito lentos, e às vezes contrarios nas materias do Governo, lhe faço mercê da propriedade e regeneia de uma Cadeira e Aula Publica, que por este mesmo Decreto sou servido crear no Rio de Janeiro, com o ordenado de 400$000 para ir exercitar, conservando os ordenados dos dous logares que até agora tem occupado na Bahia. As Juntas da Fazenda de uma e de outra Capitania o tenham assim entendido e fazão executar.",
        "data_assinatura": "Bahia 23 de Fevereiro de 1808.",
        "assinatura": "Com a rubrica do Príncipe Regente Nosso Senhor."
      }
    ]
```

### 3ª Versão de Prompt

```markdown

Você é um especialista em documentos históricos brasileiros dos séculos XVIII e XIX, com domínio em paleografia e conhecimento em legislação colonial e imperial.

Analise os textos fornecidos contidos em imagens de páginas digitalizadas de coletâneas de leis ou atas oficiais e extraia cada ato normativo individual no seguinte formato JSON estruturado:

{
  "epigrafe": "[TIPO DO DOCUMENTO] [DATA POR EXTENSO]",
  "tipo": "[ALVARÁ / DECRETO / CARTA RÉGIA / ETC.]",
  "data": "[DATA NO FORMATO ISO: YYYY-MM-DD]",
  "ementa": "[RESUMO CONCISO DO DOCUMENTO EM UMA FRASE, UTILIZANDO LINGUAGEM CONTEMPORÂNEA COM TERMOS JURÍDICOS HISTÓRICOS]",
  "content": "[TEXTO INTEGRAL DO DOCUMENTO, MANTENDO GRAFIA ARCAICA E FORMATAÇÃO ORIGINAL]",
  "data_assinatura": "[LOCAL E DATA DA ASSINATURA POR EXTENSO]",
  "assinatura": "[NOME DO AUTORIDADE OU TEXTO COMPLETO DA ASSINATURA/RUBRICA]"
}

### Regras obrigatórias:
1. Mantenha rigorosamente o texto original em português arcaico, incluindo grafia antiga (ex: “commercio”, “sciencia”, “annuas”).
2. Converta datas para o formato ISO (YYYY-MM-DD) sempre que possível.
3. A ementa deve ser concisa (uma única frase) e descrever com clareza o conteúdo jurídico do documento, mantendo termos técnicos históricos.
4. Remova elementos gráficos indesejados: cabeçalhos, números de página, ilustrações ou marcas de digitalização.
5. Trate cada ato normativo como um objeto JSON separado, mesmo que ocupe múltiplas páginas.
6. Para documentos longos que se estendem por mais de uma imagem, una o conteúdo completo no mesmo objeto JSON, mantendo a integridade textual.
7. Preservar particularidades ortográficas, sinais de pontuação antigos e formas de tratamento histórico (ex: “Vossa Alteza”, “meus vassallos”, “heis por bem ordenar”).
8. Garanta compatibilidade com UTF-8, preservando caracteres especiais e acentuação conforme o original.

### Saída esperada:
Retorne apenas um único arquivo JSON contendo um array com todos os documentos extraídos, conforme o modelo acima. Exemplo:

[
  {
    "epigrafe": "Alvará de 22 de Abril de 1808",
    "tipo": "ALVARÁ",
    "data": "1808-04-22",
    "ementa": "Criação de um tribunal no Brasil para decidir questões da Mesa do Desembargo do Paço, Consciência e Ordens, e Conselho do Ultramar.",
    "content": "Eu o Principe Regente faço saber aos que o presente Alvará virem...",
    "data_assinatura": "Palacio do Rio de Janeiro em 22 de Abril de 1808.",
    "assinatura": "PRINCIPE com guarda.\n\nD. Fernando José de Portugal."
  },
  ...
]

⚠️ Importante: Não adicione explicações, comentários ou formatação adicional — retorne apenas o JSON puro e funcional.

```
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



## Referências

 - N/A (Caso haja referências podem ser listadas aqui)


---
Copyright &copy; **incolume.com.br** since 2010
