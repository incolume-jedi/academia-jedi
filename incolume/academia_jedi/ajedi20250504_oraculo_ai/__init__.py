"""Module oracle."""

from typing import Final
import streamlit as st
from langchain.memory import ConversationBufferMemory


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
            'gemma2-9b-it', 'llama-3.3-70b-versatile', 'whisper-large-v3-turbo', 'distil-whisper-large-v3-en',
        ],
    },
    'OpenAI':{
        'modelos': [
            'gpt-4o-mini',
        'o4-mini',
        ],
    },
}

cache_memory = ConversationBufferMemory()
cache_memory.chat_memory.add_user_message('Olá')
cache_memory.chat_memory.add_ai_message('Olá, sou o oráculo. Como posso ajudá-lo?')

MESSAGES = [
    ('user', 'Olá'),
    ('agent', 'Olá, sou o oráculo. Como posso ajudá-lo?'),
]

def pg_chat():
    """Chat with the oracle."""
    st.header("Oracle incolume", divider=True)
    memoria = st.session_state.get("memoria", cache_memory)

    for mensagem in memoria.buffer_as_messages:
        chat = st.chat_message(name=mensagem.type )
        chat.markdown(mensagem.content)

    input_text = st.chat_input("Digite sua mensagem aqui..")
    if input_text:
        memoria.chat_memory.add_user_message(input_text)
        st.session_state['memoria'] = memoria
        st.rerun()

def sidebar():
    """Sidebar for the oracle."""
    tabs = st.tabs(['Upload de Arquivos', 'Seleção de Modelos'])
    with tabs[0]:
        st.header("Upload de Arquivos")
        source_selected = st.selectbox(
            label="Selecione o tipo de arquivo",
            options=SOURCES,
            index=0,
        )
        if source_selected == 'Site':
            selected = st.text_input('Digite a URL do site')
        if source_selected == 'Youtube':
            selected = st.text_input('Digite a URL do vídeo')
        if source_selected == 'CSV':
            selected = st.file_uploader(
                label="Selecione o arquivo CSV",
                type=['.csv'])
        if source_selected == 'PDF':
            selected = st.file_uploader(
                label="Selecione o arquivo PDF",
                type=['.pdf'])
        if source_selected == 'Excel':
            selected = st.file_uploader(
                label="Selecione o arquivo Excel",
                type=['.xlsx'])
        if source_selected == 'TXT':
            selected = st.file_uploader(
                label="Selecione o arquivo Texto",
                type=['.txt', '.yml', '.toml', '.yaml'])
    with tabs[1]:
        provedor = st.selectbox('Selecione o provedor', MODELOS_AI.keys())
        modelo = st.selectbox(
            label="Selecione o modelo",
            options=MODELOS_AI[provedor]['modelos'],
            index=0,
        )
        api_key = st.text_input(
            label=f"Digite sua chave de API para {provedor}",
            type='password',
            value=st.session_state.get(f'api_key_{provedor}', ''),
        )
        st.session_state[f'api_key_{provedor}'] = api_key



def main():
    """Main function to run the oracle."""
    pg_chat()
    with st.sidebar:
        sidebar()


if __name__ == "__main__":
    main()
