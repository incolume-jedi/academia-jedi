"""Module oracle."""

import io
import tempfile
from pathlib import Path
from typing import Final

import streamlit as st
from icecream import ic
from incolume.academia_jedi.ajedi20250504_oraculo_ai import utils
from langchain.memory import ConversationBufferMemory
from langchain.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI

SOURCES: Final[list[str]] = [
    'CSV',
    'Excel',
    'PDF',
    'Site',
    'TXT',
    'Youtube',
]
MODELOS_AI: Final[list[str]] = {
    'Groq': {
        'modelos': [
            'gemma2-9b-it',
            'llama-3.3-70b-versatile',
            'whisper-large-v3-turbo',
            'distil-whisper-large-v3-en',
        ],
        'chat': ChatGroq,
    },
    'OpenAI': {
        'modelos': [
            'gpt-4o-mini',
            'o4-mini',
        ],
        'chat': ChatOpenAI,
    },
}

cache_memory = ConversationBufferMemory()
cache_memory.chat_memory.add_user_message('Olá')
cache_memory.chat_memory.add_ai_message(
    'Olá, sou o oráculo. Como posso ajudá-lo?',
)


def load_content(midia: str | Path, archive_type: str) -> str:
    """Load the content from the media."""
    if archive_type == 'site':
        document = utils.load_web(midia)
    if archive_type == 'youtube':
        document = utils.load_yt(midia)
    if archive_type == 'pdf':
        with tempfile.NamedTemporaryFile(
            suffix='.pdf',
            delete=False,
        ) as tmp_file:
            tmp_file.write(midia.read())
            midia = Path(tmp_file.name)
        document = utils.load_pdf(midia)
    if archive_type == 'csv':
        with tempfile.NamedTemporaryFile(
            suffix='.CSV',
            delete=False,
        ) as tmp_file:
            tmp_file.write(midia.read())
            midia = Path(tmp_file.name)
        document = utils.load_csv(midia)
    if archive_type == 'txt':
        with tempfile.NamedTemporaryFile(
            suffix='.txt',
            delete=False,
        ) as tmp_file:
            tmp_file.write(midia.read())
            midia = Path(tmp_file.name)
        document = utils.load_txt(midia)
    ic(f'{archive_type=}; {document=}')
    return document


def load_model(
    provedor: str,
    modelo: str,
    api_key: str,
    midia: str | Path,
    archive_type: str,
) -> None:
    """Load the model."""
    document = load_content(midia, archive_type)
    system_prompt = '''Você é um assistente amigável chamado Oráculo Incolume. 
    Você possui acesso às seguintes informações vindas de mídia {}:
    ####
    {}
    ####
    Utilize as informações fornecidas para basear as tuas respostas.

    Sempre que houver $ em suas saídas, substitua por S.

    Se a informação do documento for algo como "Just a moment..Enable JavaScript and cookies to continue" sugira ao usuário carregar novamente o Oráculo!
    '''.format(archive_type, midia)
    template = ChatPromptTemplate.from_template(
        [
            ('system', system_prompt),
            ('placeholder', '{chat_history}'),
            ('user', '{input}'),
        ]
    )
    chat = MODELOS_AI[provedor]['chat'](model=modelo, api_key=api_key)
    st.session_state['chat'] = chat


def pg_chat():
    """Chat with the oracle."""
    st.header('Oracle incolume', divider=True)
    chat_agent = st.session_state.get('chat')
    memoria = st.session_state.get('memoria', cache_memory)

    for mensagem in memoria.buffer_as_messages:
        chat = st.chat_message(name=mensagem.type)
        chat.markdown(mensagem.content)

    input_text = st.chat_input('Digite sua mensagem aqui..')
    if input_text:
        memoria.chat_memory.add_user_message(input_text)
        resposta = chat_agent.invoke(input_text).content
        memoria.chat_memory.add_ai_message(resposta)
        st.session_state['memoria'] = memoria
        st.rerun()


def sidebar():
    """Sidebar for the oracle."""
    tabs = st.tabs(['Upload de Arquivos', 'Seleção de Modelos'])
    selectors = {
        'csv': lambda: st.file_uploader(
            label='Selecione o arquivo CSV',
            type=['.csv'],
        ),
        'excel': lambda: st.file_uploader(
            label='Selecione o arquivo Excel',
            type=['.xlsx'],
        ),
        'pdf': lambda: st.file_uploader(
            label='Selecione o arquivo PDF',
            type=['.pdf'],
        ),
        'site': lambda: st.text_input('Digite a URL do site'),
        'toml': lambda: st.file_uploader(
            label='Selecione o arquivo Texto',
            type=['.toml'],
        ),
        'txt': lambda: st.file_uploader(
            label='Selecione o arquivo Texto',
            type=['.txt'],
        ),
        'yml': lambda: st.file_uploader(
            label='Selecione o arquivo Texto',
            type=['.yml', '.yaml'],
        ),
        'youtube': lambda: st.text_input('Digite a URL do vídeo'),
    }
    with tabs[0]:
        st.header('Upload de Arquivos')
        source_selected = st.selectbox(
            label='Selecione o tipo de arquivo',
            options=selectors.keys(),
            index=0,
        )
        selected = selectors.get(source_selected.casefold())()

    with tabs[1]:
        provedor = st.selectbox('Selecione o provedor', MODELOS_AI.keys())
        modelo = st.selectbox(
            label='Selecione o modelo',
            options=MODELOS_AI[provedor]['modelos'],
            index=0,
        )
        api_key = st.text_input(
            label=f'Digite sua chave de API para {provedor}',
            type='password',
            value=st.session_state.get(f'api_key_{provedor}', ''),
        )
        st.session_state[f'api_key_{provedor}'] = api_key

    if st.button('Incializar agente', use_container_width=True):
        load_model(
            provedor=provedor,
            modelo=modelo,
            api_key=api_key,
            midia=selected,
            archive_type=source_selected,
        )


def main():
    """Main function to run the oracle."""
    pg_chat()
    with st.sidebar:
        sidebar()


if __name__ == '__main__':
    main()
