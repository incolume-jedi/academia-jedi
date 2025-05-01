"""Email with python."""

import json
import pprint
from dataclasses import asdict, dataclass
from datetime import datetime
from pathlib import Path
from typing import Final

from icecream import ic
from imbox import Imbox
from incolume.academia_jedi import logger

CREDENTIALS_PATH: Final[Path] = (
    Path(__file__).parents[3] / 'credentials' / 'credentials.json'
)
SMTP_SERVER: Final[str] = 'smtp.google.com'
IMAP_SERVER: Final[str] = 'imap.gmail.com'

logger.info(ic(f'{CREDENTIALS_PATH=}, {SMTP_SERVER=}, {IMAP_SERVER=}'))


@dataclass
class Email:
    """Email class."""

    username: str
    password: str
    hostname: str = 'imap.gmail.com'

    def __post_init__(self):
        """Post init method."""

    def to_dict(self) -> dict:
        """Convert the class to a dictionary."""
        return asdict(self)


def get_credentials(credentials: Path | None = None) -> dict:
    """Get the credentials from the credentials.json file."""
    credentials = credentials or CREDENTIALS_PATH
    logger.debug(ic(f'{credentials=}'))
    with credentials.open() as file:
        credentials_data = json.load(file)

    return {
        'hostname': IMAP_SERVER,
        'username': credentials_data['email'],
        'password': credentials_data['google_password'],
    }


def get_email_0(credentials: Path | None = None) -> list:
    """Get the email from the credentials.json file."""
    with Imbox(**get_credentials(credentials)) as inbox:
        messages = inbox.messages(unread=True)  # Get unread messages
        if not messages:
            logger.info(ic('No unread messages'))
            return []
        logger.info(ic(len(messages)))
    return messages


def get_email_1(credentials: Path | None = None) -> str:
    """Get the email from the credentials.json file."""
    with Imbox(**get_credentials(credentials)) as inbox:
        messages = inbox.messages(unread=True)
        for message in messages[-1]:
            print(message)


def get_email_2(credentials: Path | None = None) -> str:
    """Get the email from the credentials.json file."""
    with Imbox(**get_credentials(credentials)) as inbox:
        messages = inbox.messages(subject='Tempmail')[0]
        body = messages[1].body['plain'][0]
        return body


def get_email_3(credentials: Path | None = None) -> str:
    """Get the email from the credentials.json file."""
    timestamp = '2023-01-01'

    with Imbox(**get_credentials(credentials)) as inbox:
        messages = inbox.messages(date__gt=timestamp)[0]
        return ic(messages)


def get_email_4(credentials: Path | None = None) -> str:
    """Get the email from the credentials.json file."""
    timestamp = '2010-01-01'

    with Imbox(**get_credentials(credentials)) as inbox:
        messages = inbox.messages(date__on=timestamp)
        for msg in messages:
            msg.delete()


def get_email_8(credentials: Path | None = None) -> str:
    credentials = credentials or CREDENTIALS_PATH
    with credentials.open() as f:
        credentials_data = json.load(f)

    host = 'imap.gmail.com'
    email = credentials_data['email']
    password = credentials_data['google_password']

    start_date = datetime(2023, 1, 1)
    with Imbox(host, username=email, password=password) as imbox:
        # Abrindo a caixa de emails 2023
        messages = imbox.messages(date__gt=start_date)

    # Pegar apenas um email
    for uid, message in messages:
        atual = message
        break

    # O que é?
    print(atual)
    # Quais são as chaves que temos?
    print(atual.keys())
    # Diferença date x parsed_date
    print(atual.date)
    print(atual.parsed_date)
    # Vamos explorar as chaves
    atual.sent_from
    atual.sent_to
    atual.subject
    atual.headers
    atual.message_id
    atual.body
    atual.body['plain']
    atual.body['html']
    atual.attachments


def get_email_5(credentials: Path | None = None) -> list:
    """Get the email from the credentials.json file."""
    credentials = credentials or CREDENTIALS_PATH
    with credentials.open() as f:
        credentials_data = json.load(f)

    host = 'imap.gmail.com'
    email = credentials_data['email']
    password = credentials_data['google_password']

    start_date = datetime(2023, 1, 1)

    with Imbox(**get_credentials()) as imbox:
        # Buscar e-mails a partir de uma data específica
        messages = imbox.messages(date__gt=start_date)

    imbox_messages_uids_3000 = imbox.messages(uid__range='3000:*')
    print(len(imbox_messages_uids_3000))

    for mensagem in messages:
        atual = ic(mensagem)
        break
        # uid = atual[0]
        # email = atual[1]
        # print(f'TITULO DO EMAIL: {email.subject}')
        # print(f'DATA DO EMAIL: {email.date}')
        # imbox.delete(uid)
        # for uid, message in messages:
        #
        # Deletar todas mensagens coletadas
        #
        imbox.delete(uid)
        #
        #
        # Marcar as mensagens como lidos
    # imbox.mark_seen(uid)


def run():
    """Run the script."""
    """
    get_email_0()
    get_email_1()
    get_email_2()
    get_email_3()
    get_email_4()
    """
    get_email_5()


if __name__ == '__main__':
    run()
