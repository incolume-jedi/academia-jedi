"""Exemplo de integração entre LangChain e Hugging Face.

Este script demonstra como utilizar modelos de linguagem do
Hugging Face através da LangChain.

Autor: Manus
Data: 22/05/2025
"""
# ruff: noqa: BLE001 T201

from config import settings
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
from langchain_huggingface import HuggingFaceEndpoint


def configurar_llm_huggingface(
    modelo='google/flan-t5-small',
    temperatura=0.7,
    max_tokens=256,
):
    """Configura uma instância de LLM do Hugging Face usando a LangChain.

    Args:
        modelo (str): Nome do modelo no Hugging Face Hub
        temperatura (float): Controla a aleatoriedade das respostas (0.0 a 1.0)
        max_tokens (int): Número máximo de tokens na resposta

    Returns:
        HuggingFaceEndpoint: Instância do LLM configurada
    """
    return HuggingFaceEndpoint(
        repo_id=modelo,
        # Substitua pelo seu token
        huggingfacehub_api_token=settings.huggingfacehub_api_token,
        model_kwargs={'temperature': temperatura, 'max_length': max_tokens},
    )


def criar_chain_simples(llm, template):
    """Cria uma chain simples com o LLM e um template de prompt.

    Args:
        llm: Instância do LLM
        template (str): Template do prompt

    Returns:
        LLMChain: Chain configurada
    """
    prompt = PromptTemplate(input_variables=['pergunta'], template=template)
    return LLMChain(llm=llm, prompt=prompt)


def exemplo_chain_qa():
    """Exemplo de uso de uma chain de perguntas e respostas."""
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
    return chain.run(pergunta='Quais são os planetas do sistema solar?')


def exemplo_com_memoria():
    """Exemplo usando memória para manter contexto de conversas."""
    # Criar o LLM
    llm = configurar_llm_huggingface(modelo='google/flan-t5-base')

    # Template para conversação
    template = """
    A conversa até agora:
    {chat_history}

    Humano: {input}
    IA:
    """

    # Configurar memória de conversação
    memoria = ConversationBufferMemory(memory_key='chat_history')

    # Criar prompt
    prompt = PromptTemplate(
        input_variables=['chat_history', 'input'],
        template=template,
    )

    # Criar chain de conversação com memória
    conversa = LLMChain(llm=llm, prompt=prompt, memory=memoria, verbose=True)

    # Simular uma conversa
    resposta1 = conversa.predict(input='Olá, meu nome é João.')
    resposta2 = conversa.predict(input='Qual é o meu nome?')

    return resposta1, resposta2


def exemplo_rag_com_huggingface():
    """Exemplo de RAG.

    (Retrieval Augmented Generation) usando LangChain e Hugging Face.
    """
    from langchain.chains import RetrievalQA
    from langchain.embeddings import HuggingFaceEmbeddings
    from langchain.text_splitter import CharacterTextSplitter
    from langchain.vectorstores import FAISS

    # Texto de exemplo para criar nossa base de conhecimento
    documentos = [
        'O Brasil é o maior país da América do Sul.',
        'A capital do Brasil é Brasília.',
        'O Brasil tem uma população de aproximadamente'
        ' 213 milhões de pessoas.',
        'A Amazônia é a maior floresta tropical do mundo e está localizada'
        ' principalmente no Brasil.',
    ]

    # Dividir texto em chunks
    text_splitter = CharacterTextSplitter(chunk_size=100, chunk_overlap=0)
    textos = text_splitter.create_documents(documentos)

    # Criar embeddings usando modelo do Hugging Face
    embeddings = HuggingFaceEmbeddings(
        model_name='sentence-transformers/all-MiniLM-L6-v2',
    )

    # Criar base de conhecimento vetorial
    db = FAISS.from_documents(textos, embeddings)

    # Configurar LLM
    llm = configurar_llm_huggingface()

    # Criar chain de RAG
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type='stuff',
        retriever=db.as_retriever(),
    )

    # Consultar a base de conhecimento
    return qa_chain.run('Qual é a capital do Brasil?')


def exemplo_agente_com_ferramentas():
    """Exemplo de um agente com ferramentas usando LangChain e Hugging Face."""
    from langchain.agents import AgentType, initialize_agent, load_tools

    # Criar o LLM
    llm = configurar_llm_huggingface(modelo='google/flan-t5-large')

    # Carregar ferramentas básicas
    ferramentas = load_tools(['llm-math'], llm=llm)

    # Inicializar o agente
    agente = initialize_agent(
        tools=ferramentas,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
    )

    # Executar o agente
    return agente.run('Qual é a raiz quadrada de 144 mais 25?')


def main():
    """Função principal para demonstrar os exemplos."""
    print('Demonstração de integração LangChain com Hugging Face')
    print('\n1. Exemplo simples de pergunta e resposta:')
    try:
        resposta = exemplo_chain_qa()
        print(f'Resposta: {resposta}')
    except Exception as e:
        print(f'Erro no exemplo simples: {e}')

    print('\n2. Exemplo com memória de conversação:')
    try:
        resposta1, resposta2 = exemplo_com_memoria()
        print(f'Primeira resposta: {resposta1}')
        print(f'Segunda resposta: {resposta2}')
    except Exception as e:
        print(f'Erro no exemplo com memória: {e}')

    print('\n3. Exemplo de RAG com Hugging Face:')
    try:
        resposta = exemplo_rag_com_huggingface()
        print(f'Resposta RAG: {resposta}')
    except Exception as e:
        print(f'Erro no exemplo de RAG: {e}')

    print('\n4. Exemplo de agente com ferramentas:')
    try:
        resultado = exemplo_agente_com_ferramentas()
        print(f'Resultado do agente: {resultado}')
    except Exception as e:
        print(f'Erro no exemplo de agente: {e}')


if __name__ == '__main__':
    main()
