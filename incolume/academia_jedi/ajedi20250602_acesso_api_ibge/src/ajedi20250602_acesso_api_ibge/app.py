"""Web app."""

import streamlit as st
from incolume.academia_jedi.ajedi20250602_acesso_api_ibge import get_nome
from icecream import ic


def main():
    """ Main function to run the Streamlit app."""
    st.title("Web App Nomes")
    st.write("Dados da IBGE API")

    nome = st.text_input('Consulte um nome')
    if not nome:
        st.stop()

    ic(get_nome(nome=nome))




if __name__ == '__main__':
    main()


