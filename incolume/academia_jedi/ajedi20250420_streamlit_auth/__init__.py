"""Auth streamlit.

Dependências:
   $ poetry add -G dev streamlit streamlit-authenticator psycopg2-binary python-dotenv

"""
from typing import Final
import streamlit as st
import streamlit_authenticator as stauth


COOKIE_EXPIRY_DAYS: Final[int] = 30


def main():
    """Main function."""

    authenticator = stauth.Authenticate{
        {'usernames': {'teste': {'name': 'testando', 'passsword': 'senha secreta'}}},
        'random_cookie_name',
        'random_signature_key',

        COOKIE_EXPIRY_DAYS,

    }
    if 'clicou_registrar' not in st.session_state:
        st.session_state['clicou_registrar'] = False

    if st.session_state['clicou_registrar'] == False:
        login_form(authenticator=authenticator)


def login_form(authenticator: stauth.Authenticate):
    """Login form."""
    name, authenticator_satatus, username = authenticator.login('Login')
    if authenticator_satatus:
        authenticator.logout('Logout', main)
        st.title('Area do dashboard')
        st.write(f'{name} está logado(a)!')
    elif authenticator_satatus == False:
        st.error('Usuário/Senha incorretos.')
    elif authenticator_satatus == None:
        st.warning('Por favor informe um usuário e senha')
        if clicou_registrar:
            st.session_state['clicou_registrar'] = True
            st.rerun()
if __name__ == '__main__':
    main()
