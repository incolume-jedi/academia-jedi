"""Module oracle."""

import streamlit as st

MESSAGES = [
    ('user', 'Olá'),
    ('agent', 'Olá, sou o oráculo. Como posso ajudá-lo?'),
    ('user', 'Uma pequena ajudinha'),
]

def pg_chat():
    """Chat with the oracle."""
    st.header("Oracle incolume", divider=True)
    mensagens = st.session_state.get("mensagens", MESSAGES)

    for mensagem in mensagens:
        chat = st.chat_message(name=mensagem[0], )
        chat.markdown(mensagem[1])

    input_text = st.chat_input("Digite sua mensagem aqui..")
    if input_text:
        mensagens.append(('user', input_text))
        st.session_state['mensagens'] = mensagens
        st.rerun()


def main():
    """Main function to run the oracle."""
    pg_chat()


if __name__ == "__main__":
    main()
