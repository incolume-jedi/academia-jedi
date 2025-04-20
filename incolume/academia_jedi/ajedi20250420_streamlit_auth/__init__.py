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
        if 'clicou_registrar':
            st.session_state['clicou_registrar'] = True
            st.rerun()

def confirm_msg():
    """Confirm msg."""
    hashed_password = stauth.Hasher([st.session_state.pswrd]).generate()
    if st.session_state.pswrd != st.session_state.confirm_pswrd:
        st.warning('Senhas não conferem')
    elif 'consulta_nome()':
        st.warning('Nome de usuário já cadastrado.')
    else:
        'add_registro()'
        st.success('Registro efetuado!')


def usuario_form():
    """Formulário de login."""
    with st.form(key='formulario', clear_on_submit=True):
        nome = st.text_input('Nome', key='nome')
        username = st.text_input('Usuário', key='user')
        password = st.text_input('Senha', key='pswrd', type='password')
        confirm_password = st.text_input('Confirme senha', key='confir_pswrd', type='password')
        submit = st.form_submit_button(
            'Salvar', on_click=confirm_msg,
        )
        clicou_fazer_login = st.button('Fazer login?')
        if clicou_fazer_login:
            st.session_state['clicou_fazer_login'] = False
            st.rerun()

if __name__ == '__main__':
    main()
