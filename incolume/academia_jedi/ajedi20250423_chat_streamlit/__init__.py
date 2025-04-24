"""Chat streamlit."""

# ruff: noqa: E501
from __future__ import annotations

import datetime as dt
import pickle
import time
from pathlib import Path

import streamlit as st
from config import settings
from icecream import ic
from incolume.academia_jedi import logger
from pytz import timezone
from unidecode import unidecode

icons: list[str] = [
    '<svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#ff0000"><path d="M360-390q-21 0-35.5-14.5T310-440q0-21 14.5-35.5T360-490q21 0 35.5 14.5T410-440q0 21-14.5 35.5T360-390Zm240 0q-21 0-35.5-14.5T550-440q0-21 14.5-35.5T600-490q21 0 35.5 14.5T650-440q0 21-14.5 35.5T600-390ZM480-160q134 0 227-93t93-227q0-24-3-46.5T786-570q-21 5-42 7.5t-44 2.5q-91 0-172-39T390-708q-32 78-91.5 135.5T160-486v6q0 134 93 227t227 93Zm0 80q-83 0-156-31.5T197-197q-54-54-85.5-127T80-480q0-83 31.5-156T197-763q54-54 127-85.5T480-880q83 0 156 31.5T763-763q54 54 85.5 127T880-480q0 83-31.5 156T763-197q-54 54-127 85.5T480-80Zm-54-715q42 70 114 112.5T700-640q14 0 27-1.5t27-3.5q-42-70-114-112.5T480-800q-14 0-27 1.5t-27 3.5ZM177-581q51-29 89-75t57-103q-51 29-89 75t-57 103Zm249-214Zm-103 36Z"/></svg>',
    '<svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#e3e3e3"><path d="M620-520q25 0 42.5-17.5T680-580q0-25-17.5-42.5T620-640q-25 0-42.5 17.5T560-580q0 25 17.5 42.5T620-520Zm-280 0q25 0 42.5-17.5T400-580q0-25-17.5-42.5T340-640q-25 0-42.5 17.5T280-580q0 25 17.5 42.5T340-520Zm140 260q68 0 123.5-38.5T684-400H276q25 63 80.5 101.5T480-260Zm0 180q-83 0-156-31.5T197-197q-54-54-85.5-127T80-480q0-83 31.5-156T197-763q54-54 127-85.5T480-880q83 0 156 31.5T763-763q54 54 85.5 127T880-480q0 83-31.5 156T763-197q-54 54-127 85.5T480-80Zm0-400Zm0 320q134 0 227-93t93-227q0-134-93-227t-227-93q-134 0-227 93t-93 227q0 134 93 227t227 93Z"/></svg>',
    '<svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#1f1f1f"><path d="M580-490q-21 0-35.5-14.5T530-540q0-21 14.5-35.5T580-590q21 0 35.5 14.5T630-540q0 21-14.5 35.5T580-490Zm-200 0q-21 0-35.5-14.5T330-540q0-21 14.5-35.5T380-590q21 0 35.5 14.5T430-540q0 21-14.5 35.5T380-490Zm100 210q-60 0-108.5-33T300-400h360q-23 54-71.5 87T480-280Zm0 160q-75 0-140.5-28.5t-114-77q-48.5-48.5-77-114T120-480q0-75 28.5-140.5t77-114q48.5-48.5 114-77T480-840q75 0 140.5 28.5t114 77q48.5 48.5 77 114T840-480q0 75-28.5 140.5t-77 114q48.5 48.5 114 77T480-120Zm0-80q116 0 198-82t82-198q0-116-82-198t-198-82h12q6 0 12 2z"/></svg>',
    '<svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#e3e3e3"><path d="M480-480q-66 0-113-47t-47-113q0-66 47-113t113-47q66 0 113 47t47 113q0 66-47 113t-113 47ZM160-160v-112q0-34 17.5-62.5T224-378q62-31 126-46.5T480-440q66 0 130 15.5T736-378q29 15 46.5 43.5T800-272v112H160Zm80-80h480v-32q0-11-5.5-20T700-306q-54-27-109-40.5T480-360q-56 0-111 13.5T260-306q-9 5-14.5 14t-5.5 20v32Zm240-320q33 0 56.5-23.5T560-640q0-33-23.5-56.5T480-720q-33 0-56.5 23.5T400-640q0 33 23.5 56.5T480-560Zm0-80Zm0 400Z"/></svg>',
]


def filename_chat(user1: str, user2: str) -> Path:
    """Create filename based in chat members."""
    x = Path(__file__).parent.joinpath(
        'mensagens',
        '-'.join(
            unidecode(u).replace(' ', '_').casefold()
            for u in sorted([user1, user2])
        ),
    )
    x.parent.mkdir(parents=True, exist_ok=True)
    return x.with_stem(
        f'{x.stem}-{dt.datetime.now(tz=timezone(settings.tz)):%Y%m%d}',
    ).with_suffix('.pkl')


def write_msg(user1: str, user2: str, message: dict) -> Path:
    """Write messages."""
    with (filename := filename_chat(user1, user2)).open('wb') as f:
        pickle.dump(message, f)
    return filename


def read_msg(user1: str, user2: str) -> list:
    """Read messagens."""
    result = []
    try:
        with filename_chat(user1, user2).open('rb') as f:
            result = pickle.load(f)  # noqa: S301
    except FileNotFoundError as e:
        logger.exception(e.strerror)
    return result


def filename_user(username: str, path: Path = 'users') -> Path:
    """Filename users."""
    path = path or 'users'
    filename = (
        Path(__file__).parent
        / path
        / f'{unidecode(username).replace(' ', '_').casefold()}.pkl'
    )
    ic(filename)
    filename.parent.mkdir(exist_ok=True, parents=True)
    return filename


def check_senha(nome: str, senha: str, path: None | Path = None) -> bool:
    """Check password."""
    filename = filename_user(nome, path)
    try:
        with filename.open('rb') as f:
            data = pickle.load(f)  # noqa: S301
    except FileNotFoundError:
        return False

    return (data['username'] == nome) and (data['password'] == senha)


def __login_user(nome: str, senha: str) -> None:
    """Login user."""
    if check_senha(nome, senha):
        time.sleep(2)
        st.session_state['userlogged'] = nome.upper()
        st.success('Loggin efetuado com sucesso')
        time.sleep(2)
        change_pg('chat')
    else:
        st.error('Erro ao logar')


def create_new_user(nome: str, senha: str, path: Path = 'users') -> bool:
    """Create new user."""
    filename = filename_user(nome, path)
    if filename.exists():
        return False
    with filename.open('wb') as f:
        pickle.dump({'username': nome, 'password': senha}, f)
    return filename.is_file()


def users_all(path: Path | None = None) -> list[str]:
    """List all users.

    Returns:
        list[str]: _description_
    """
    path = path or Path(__file__).parent / 'users'
    return [file.stem for file in path.glob('*.pkl')]


def change_pg(page_name: str) -> None:
    """Change page."""
    st.session_state['atualpage'] = page_name
    st.rerun()


def pg_login():
    """Login page."""
    st.header('Bem vindo ao Messenger de JEDI Incolume.', divider=True)
    tab1, tab2 = st.tabs(['Entrar', 'Cadastrar'])
    with tab1.form(key='login'):
        nome = st.text_input('Digite teu nome de usuário')
        senha = st.text_input('Digite tua senha')
        if st.form_submit_button('Entrar'):
            __login_user(nome, senha)

    with tab2.form(key='cadastro'):
        nome = st.text_input('Cadastre novo de usuário')
        senha = st.text_input('Digite nova senha', type='password')
        senha_confirm = st.text_input(
            'Digite novamente a nova senha',
            type='password',
        )
        if (
            st.form_submit_button('Cadastrar')
            and (nome != '')
            and (senha == senha_confirm)
        ):
            create_new_user(nome, senha)
            st.success('Usuário cadastrado com sucesso.')
            time.sleep(2)
            st.session_state['userlogged'] = nome.upper()
            change_pg('chat')
        elif not nome and senha:
            st.error('Nome de usuário inválido.')
        elif senha != senha_confirm:
            st.error('Senhas não conferem.')


def pg_chat():
    """Page chat."""
    st.title('Jedi Chat')
    st.divider()

    userlogged = st.session_state['userlogged']
    userchat = st.session_state.get('userchat')

    mensagens = read_msg(user1=userlogged, user2=userchat)

    for mensagem in mensagens:
        user = (
            'user'
            if mensagem.get('username') == userlogged
            else mensagem.get('username')
        )
        avatar = (
            '<svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#e3e3e3"><path d="M480-480q-66 0-113-47t-47-113q0-66 47-113t113-47q66 0 113 47t47 113q0 66-47 113t-113 47ZM160-160v-112q0-34 17.5-62.5T224-378q62-31 126-46.5T480-440q66 0 130 15.5T736-378q29 15 46.5 43.5T800-272v112H160Zm80-80h480v-32q0-11-5.5-20T700-306q-54-27-109-40.5T480-360q-56 0-111 13.5T260-306q-9 5-14.5 14t-5.5 20v32Zm240-320q33 0 56.5-23.5T560-640q0-33-23.5-56.5T480-720q-33 0-56.5 23.5T400-640q0 33 23.5 56.5T480-560Zm0-80Zm0 400Z"/></svg>'
            if mensagem['username'] == userlogged
            else '<svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#1f1f1f"><path d="M580-490q-21 0-35.5-14.5T530-540q0-21 14.5-35.5T580-590q21 0 35.5 14.5T630-540q0 21-14.5 35.5T580-490Zm-200 0q-21 0-35.5-14.5T330-540q0-21 14.5-35.5T380-590q21 0 35.5 14.5T430-540q0 21-14.5 35.5T380-490Zm100 210q-60 0-108.5-33T300-400h360q-23 54-71.5 87T480-280Zm0 160q-75 0-140.5-28.5t-114-77q-48.5-48.5-77-114T120-480q0-75 28.5-140.5t77-114q48.5-48.5 114-77T480-840q75 0 140.5 28.5t114 77q48.5 48.5 77 114T840-480q0 75-28.5 140.5t-77 114q-48.5 48.5-114 77T480-120Zm0-80q116 0 198-82t82-198q0-116-82-198t-198-82h-12q-6 0-12 2-6 6-8 13t-2 15q0 21 14.5 35.5T496-680q9 0 16.5-3t15.5-3q12 0 20 9t8 21q0 23-21.5 29.5T496-620q-45 0-77.5-32.5T386-730v-6q0-3 1-8-83 30-135 101t-52 163q0 116 82 198t198 82Zm0-280Z"/></svg>'
        )
        chat = st.chat_message(user, avatar=avatar)
        chat.markdown(mensagem.get('content'))

    newmsg = st.chat_input('Digite uma mensagem: ')
    if newmsg:
        msg_dict = {
            'username': userlogged,
            'content': newmsg,
        }
        chat = st.chat_message('user')
        chat.markdown(msg_dict['content'])
        mensagens.append(msg_dict)
        write_msg(user1=userlogged, user2=userchat, message=mensagens)


def starting():
    """Start configuration."""
    if 'atualpage' not in st.session_state:
        st.session_state['atualpage'] = 'login'

    if 'userlogged' not in st.session_state:
        st.session_state['userlogged'] = ''

    if 'userchat' not in st.session_state:
        st.session_state['userchat'] = ''


def main():
    """Manager application."""
    navigation: dict[str, callable] = {
        'login': pg_login,
        'chat': pg_chat,
    }

    starting()

    navigation[st.session_state['atualpage']]()


if __name__ == '__main__':
    main()
