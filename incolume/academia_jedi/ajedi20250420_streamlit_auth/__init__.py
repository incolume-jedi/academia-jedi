"""Auth streamlit.

Dependências:
   $ poetry add -G dev streamlit streamlit-authenticator psycopg2-binary python-dotenv

"""
# ruff: noqa: E501

from time import sleep
from typing import Final

import streamlit as st
import streamlit_authenticator as stauth
from icecream import ic
from incolume.academia_jedi.ajedi20250420_streamlit_auth.dependencies import (
    add_registro,
    consulta,
    consulta_geral,
    cria_tabela,
)
from psycopg2 import OperationalError
from psycopg2.errors import UndefinedTable

COOKIE_EXPIRY_DAYS: Final[int] = 30


def main():
    """Main function."""
    try:
        consulta_geral()
    except (UndefinedTable, OperationalError):
        cria_tabela()

    db_query = consulta_geral()

    registros = {'usernames': {}}
    for data in db_query:
        registros['usernames'][data[1]] = {
            'name': data[0],
            'password': data[2],
        }

    authenticator = stauth.Authenticate(
        registros,
        'random_cookie_name',
        'random_signature_key',
        COOKIE_EXPIRY_DAYS,
    )
    if 'clicou_registrar' not in st.session_state:
        st.session_state['clicou_registrar'] = False

    if st.session_state['clicou_registrar'] is False:
        login_form(authenticator=authenticator)
    else:
        usuario_form()


def login_form(authenticator):
    """Formulário de autenticação."""
    # name, authentication_status, username = authenticator.login('Login')
    # ic(f'{name=} {authentication_status=}, {username=}')
    # if authentication_status:
    #     authenticator.logout('Logout', 'main')
    #     st.write(f'*{name} está logado!*')
    #     st.title('AREA DO DASHBOARD')
    # elif authentication_status is False:
    #     st.error('Usuário ou senha incorretos')
    # elif authentication_status is None:
    #     st.warning('Insira um nome de usuário e uma senha')
    #     clicou_em_registrar = st.button('Registrar')
    #     if clicou_em_registrar:
    #         st.session_state['clicou_registrar'] = True
    #         st.rerun()
    try:
        ic(authenticator.login(location='main', key='Login'))
    except Exception as e:
        st.error(e)


def confirmation_msg():
    """Mensagem de confirmação."""
    hashed_password = stauth.Hasher([st.session_state.pswrd]).generate()
    if st.session_state.pswrd != st.session_state.confirm_pswrd:
        st.warning('Senhas não conferem')
        sleep(3)
    elif consulta(st.session_state.user):
        st.warning('Nome de usuário já existe.')
        sleep(3)
    else:
        add_registro(
            st.session_state.nome,
            st.session_state.user,
            hashed_password[0],
        )
        st.success('Registro efetuado!')
        sleep(3)


def usuario_form():
    """Formulário de usuário."""
    with st.form(key='test', clear_on_submit=True):
        nome = st.text_input('Nome', key='nome')
        username = st.text_input('Usuário', key='user')
        password = st.text_input('Password', key='pswrd', type='password')
        confirm_password = st.text_input(
            'Confirm Password',
            key='confirm_pswrd',
            type='password',
        )

        submit = st.form_submit_button(
            'Salvar',
            on_click=confirmation_msg,
        )

        ic(f'{nome=} {username=} {password=} {confirm_password=} {submit=}')

    clicou_em_fazer_login = st.button('Fazer Login')
    if clicou_em_fazer_login:
        st.session_state['clicou_registrar'] = False
        st.rerun()


if __name__ == '__main__':
    main()
