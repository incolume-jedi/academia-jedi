# Acadêmia JEDI

**[Guilda JEDI Incolume](https://discord.gg/eBNamXVtBW) - Grupo Python Incolume**

**JEDI - Junta Especializada de Desenvolvimento e Inovação**
- _[Seja membro da Guilda JEDI Incolume](https://discord.gg/eBNamXVtBW)_

---

## Problema

**Converter imagens em texto através de agente de IA**

Primeiro prompt

```markdown
São paginas contém um ou mais atos normativos do governo brasileiro do século 18. Preciso que você acesse o texto identifique o encode, e mantenha o texto em português arcaico. Em cada página há um título e o número de página, remova-os.

Você como linguista especialista em língua portuguesa do século 18, me entregará um arquivo com o texto revisado e corrigido sem alteração do original.
```

```bash
    Você é um especialista em documentos históricos brasileiros do século XIX, com domínio do português arcaico e conhecimento em paleografia. Analise os textos fornecidos e extraia cada ato normativo (cartas régias, decretos, alvarás) no seguinte formato JSON:

    [
      {
        "epigrafe": "[TIPO DO DOCUMENTO] — [DATA POR EXTENSO]",
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

    Exemplo de saída esperada:
    ```json
    [
      {
        "epigrafe": "DECRETO — DE 23 DE FEVEREIRO DE 1808",
        "tipo": "DECRETO",
        "data": "1808-02-23",
        "ementa": "Criação de cadeira de Ciência Econômica no Rio de Janeiro",
        "content": "Sendo absolutamente necessario... [texto completo]",
        "data_assinatura": "Bahia 23 de Fevereiro de 1808.",
        "assinatura": "Com a rubrica do Príncipe Regente Nosso Senhor."
      }
    ]
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
