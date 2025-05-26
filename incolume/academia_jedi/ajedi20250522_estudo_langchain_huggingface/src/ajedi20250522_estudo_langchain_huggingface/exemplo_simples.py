"""Exemplo de integração entre LangChain e Hugging Face - Versão Simplificada
Este script demonstra como utilizar modelos de linguagem do Hugging Face através da LangChain.

Autor: Manus
Data: 22/05/2025
"""

# Importações necessárias
from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_huggingface import HuggingFaceEndpoint

load_dotenv()


def configurar_llm_huggingface(
    modelo='google/flan-t5-small', temperatura=0.7, max_tokens=256,
):
    """Configura uma instância de LLM do Hugging Face usando a LangChain.

    Args:
        modelo (str): Nome do modelo no Hugging Face Hub
        temperatura (float): Controla a aleatoriedade das respostas (0.0 a 1.0)
        max_tokens (int): Número máximo de tokens na resposta

    Returns:
        HuggingFaceEndpoint: Instância do LLM configurada
    """
    llm = HuggingFaceEndpoint(
        repo_id=modelo,
        huggingfacehub_api_token=settings.huggingfacehub_api_token,  # Substitua pelo seu token
        model_kwargs={'temperature': temperatura, 'max_length': max_tokens},
    )
    return llm


def criar_chain_simples(llm, template):
    """Cria uma chain simples com o LLM e um template de prompt.

    Args:
        llm: Instância do LLM
        template (str): Template do prompt

    Returns:
        LLMChain: Chain configurada
    """
    prompt = PromptTemplate(input_variables=['pergunta'], template=template)
    chain = LLMChain(llm=llm, prompt=prompt)
    return chain


def exemplo_chain_qa():
    """Exemplo de uso de uma chain de perguntas e respostas.
    """
    # Template para perguntas e respostas
    template = """
    Responda a seguinte pergunta de forma clara e concisa:

    Pergunta: {pergunta}

    Resposta:
    """

    # Criar o LLM
    llm = configurar_llm_huggingface()

    # Criar a chain
    chain = criar_chain_simples(llm, template)

    # Executar a chain com uma pergunta
    resposta = chain.run(pergunta='Quais são os planetas do sistema solar?')

    return resposta


def main():
    """Função principal para demonstrar o exemplo.
    """
    print('Demonstração de integração LangChain com Hugging Face')
    print('\nExemplo simples de pergunta e resposta:')
    try:
        resposta = exemplo_chain_qa()
        print(f'Resposta: {resposta}')
    except Exception as e:
        print(f'Erro no exemplo: {e}')


if __name__ == '__main__':
    main()
