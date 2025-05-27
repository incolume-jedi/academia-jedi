# Guia de Uso: Integração LangChain com Hugging Face

Este documento explica como utilizar os exemplos de código fornecidos para integrar
modelos de linguagem do Hugging Face com a biblioteca LangChain em Python.

Autor: Manus

Data: 22/05/2025

## Requisitos de Instalação
Para executar os exemplos, você precisará instalar as seguintes bibliotecas:

```bash
pip install langchain langchain_huggingface transformers huggingface_hub
pip install faiss-cpu sentence-transformers  # Para o exemplo de RAG
```

## Token do Hugging Face
Para utilizar os modelos do Hugging Face, você precisará de um token de API.
Obtenha seu token em: https://huggingface.co/settings/tokens

Substitua "hf_seu_token_aqui" nos exemplos pelo seu token real.

## Descrição dos Exemplos

### 1. exemplo_simples.py
Um exemplo básico que demonstra como configurar um modelo do Hugging Face
com LangChain e criar uma chain simples de perguntas e respostas.

### 2. exemplo_completo.py
Um exemplo completo que demonstra várias funcionalidades:
- Chain simples de perguntas e respostas
- Conversação com memória para manter contexto
- RAG (Retrieval Augmented Generation) com embeddings do Hugging Face
- Agente com ferramentas para resolver problemas complexos

## Como Executar os Exemplos

1. Instale as dependências necessárias
2. Substitua "hf_seu_token_aqui" pelo seu token do Hugging Face
3. Execute os scripts:

```bash
python exemplo_simples.py
# ou
python exemplo_completo.py
```

## Notas Importantes

- Os exemplos utilizam modelos leves como "google/flan-t5-small" para rápida execução
- Para melhores resultados em produção, considere modelos maiores
- A execução inicial pode ser lenta devido ao download dos modelos
- Alguns exemplos podem exigir mais memória RAM dependendo do modelo escolhido

## Personalização

Você pode personalizar os exemplos alterando:
- O modelo utilizado (parâmetro "modelo")
- A temperatura (controla aleatoriedade das respostas)
- O número máximo de tokens (controla tamanho das respostas)
- Os templates de prompt para diferentes casos de uso

## Recursos Adicionais

- Documentação LangChain: https://python.langchain.com/docs/get_started/introduction
- Hugging Face Hub: https://huggingface.co/models
- Integração LangChain-Hugging Face: https://python.langchain.com/docs/integrations/llms/huggingface
