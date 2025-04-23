"""Chat streamlit."""
# ruff: noqa: E501

import datetime as dt
import pickle
from pathlib import Path

import streamlit as st
from config import settings
from incolume.academia_jedi import logger
from pytz import timezone
from unidecode import unidecode
from icecream import ic


def read_msg(user1: str, user2: str) -> list:
    """Read messagens."""
    result = []
    try:
        with filename_chat(user1, user2).open('rb') as f:
            result = pickle.load(f)  # noqa: S301
    except FileNotFoundError as e:
        logger.exception(e.strerror)
    return result


def write_msg(user1: str, user2: str, message: dict) -> Path:
    """Write messages."""
    with (filename := filename_chat(user1, user2)).open('wb') as f:
        pickle.dump(message, f)
    return filename


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

def pg_login():
    """Login page."""
    st.title('Bem vindo ao Streamlit Messenger de JEDI Incolume.')


def pg_chat():
    """Page chat."""
    st.title('Jedi Chat')
    st.divider()

    userloged = 'Ricardo Brito'
    userchat = 'Ada Brito'

    mensagens = read_msg(user1=userloged, user2=userchat)

    for mensagem in mensagens:
        user = (
            'user'
            if mensagem.get('username') == userloged
            else mensagem.get('username')
        )
        avatar = (
            None
            if mensagem['username'] == userloged
            else '<svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#1f1f1f"><path d="M580-490q-21 0-35.5-14.5T530-540q0-21 14.5-35.5T580-590q21 0 35.5 14.5T630-540q0 21-14.5 35.5T580-490Zm-200 0q-21 0-35.5-14.5T330-540q0-21 14.5-35.5T380-590q21 0 35.5 14.5T430-540q0 21-14.5 35.5T380-490Zm100 210q-60 0-108.5-33T300-400h360q-23 54-71.5 87T480-280Zm0 160q-75 0-140.5-28.5t-114-77q-48.5-48.5-77-114T120-480q0-75 28.5-140.5t77-114q48.5-48.5 114-77T480-840q75 0 140.5 28.5t114 77q48.5 48.5 77 114T840-480q0 75-28.5 140.5t-77 114q-48.5 48.5-114 77T480-120Zm0-80q116 0 198-82t82-198q0-116-82-198t-198-82h-12q-6 0-12 2-6 6-8 13t-2 15q0 21 14.5 35.5T496-680q9 0 16.5-3t15.5-3q12 0 20 9t8 21q0 23-21.5 29.5T496-620q-45 0-77.5-32.5T386-730v-6q0-3 1-8-83 30-135 101t-52 163q0 116 82 198t198 82Zm0-280Z"/></svg>'
        )
        chat = st.chat_message(user, avatar=avatar)
        chat.markdown(mensagem.get('content'))

    newmsg = st.chat_input('Digite uma mensagem: ')
    if newmsg:
        msg_dict = {
            'username': userloged,
            'content': newmsg,
        }
        chat = st.chat_message('user')
        chat.markdown(msg_dict['content'])
        mensagens.append(msg_dict)
        write_msg(user1=userloged, user2=userchat, message=mensagens)


def main():
    """Manager application."""
    navigation: dict[str, callable] = {
        'login': pg_login,
        'chat': pg_chat,
    }
    if 'atualpage' not in st.session_state:
        st.session_state['atualpage'] = 'login'

    navigation[st.session_state['atualpage']]()


if __name__ == '__main__':
    main()
