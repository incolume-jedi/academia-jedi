"""Email with python."""

# ruff: noqa: T201 T203

from __future__ import annotations

import datetime as dt
import json
from dataclasses import asdict, dataclass
from datetime import datetime
from pathlib import Path
from pprint import pprint
from typing import Final

from config import settings
from icecream import ic
from imbox import Imbox
from incolume.academia_jedi import logger
from pytz import timezone

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


def get_credentials(credentials: Path | None = None, hostname: str = '') -> dict:
    """Get the credentials from the credentials.json file."""
    credentials = credentials or CREDENTIALS_PATH
    hostname = hostname or IMAP_SERVER
    logger.debug(ic(f'{credentials=}'))
    with credentials.open() as file:
        credentials_data = json.load(file)

    return {
        'hostname': hostname,
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
        return messages


def get_email_2(credentials: Path | None = None) -> str:
    """Get the email from the credentials.json file."""
    with Imbox(**get_credentials(credentials)) as inbox:
        messages = inbox.messages(subject='Tempmail')[0]
        return messages[1].body['plain'][0]


def get_email_3(credentials: Path | None = None) -> str:
    """Get the email from the credentials.json file."""
    timestamp = dt.datetime(
        2023,
        1,
        1,
        0,
        1,
        2,
        3456,
        tzinfo=timezone(settings.TZ),
    )

    with Imbox(**get_credentials(credentials)) as inbox:
        messages = inbox.messages(date__gt=timestamp)[0]
        return ic(messages)


def get_email_4(credentials: Path | None = None) -> str:
    """Get the email from the credentials.json file."""
    timestamp = dt.datetime(2010, 1, 1, tzinfo=timezone(settings.TZ))

    with Imbox(**get_credentials(credentials)) as inbox:
        messages = inbox.messages(date__on=timestamp)
        for msg in messages:
            msg.delete()


def get_email_8(credentials: Path | None = None) -> str:
    """Example from course.

    Args:
        credentials (Path | None, optional): _description_. Defaults to None.

    Returns:
        str: _description_
    """
    credentials = credentials or CREDENTIALS_PATH
    with credentials.open() as f:
        credentials_data = json.load(f)

    host = 'imap.gmail.com'
    email = credentials_data['email']
    password = credentials_data['google_password']

    start_date = datetime(2023, 1, 1, tzinfo=timezone(settings.TZ))
    with Imbox(host, username=email, password=password) as imbox:
        # Abrindo a caixa de emails 2023
        messages = imbox.messages(date__gt=start_date)

        # Pegar apenas um email
        for uid, message in messages:
            logger.debug(ic(f'{uid=}, {message=}'))
            atual = message
            break

    # O que é?
    pprint(atual)
    # Quais são as chaves que temos?
    pprint(atual.keys())
    # Diferença date x parsed_date
    print(atual.date)
    print(atual.parsed_date)
    # Vamos explorar as chaves
    print(
        f'\n\n{atual.sent_from=}',
        f'\n\n{atual.sent_to=}',
        f'\n\n{atual.subject=}',
        f'\n\n{atual.headers=}',
        f'\n\n{atual.message_id=}',
        f'\n\n{atual.body=}',
        f"\n\n{atual.body['plain']=}",
        f"\n\n{atual.body['html']=}",
        f'\n\n{atual.attachments=}',
    )


def get_email_9(credentials: Path | None = None) -> list:
    """Get the email from the credentials.json file.

    Consulta e deleta mensagens a partir de um parametro especificado.
    """
    credentials = credentials or CREDENTIALS_PATH

    start_date = datetime(2023, 1, 1, tzinfo=timezone(settings.TZ))

    with Imbox(**get_credentials(credentials=credentials)) as imbox:
        # Buscar e-mails a partir de uma data específica
        messages = imbox.messages(date__gt=start_date)

        imbox_messages_uids_3000 = imbox.messages(uid__range='3000:*')
        print(len(imbox_messages_uids_3000))

        for atual in messages[-1:]:
            logger.debug(ic(f'{type(atual)=}'))
            logger.debug(ic(f'{atual=}'))
            # break
            logger.debug(ic(f'{len(atual)=}'))
            uid, email = atual
            logger.debug(ic(f'{uid=}'))
            logger.debug(ic(f'{email=}'))

            print(f'TITULO DO EMAIL: {email.subject}')
            print(f'DATA DO EMAIL: {email.date}')
            # imbox.delete(uid)
            # for uid, message in messages:
                #
                # Deletar todas mensagens coletadas
                #
                # imbox.delete(uid)


def get_email_10(credentials: Path | None = None) -> list:
    """Get the email from the credentials.json file.

    Consulta e marca mensagens como lidas a partir de um parametro especificado.
    """
    credentials = credentials or CREDENTIALS_PATH

    start_date = datetime(2021, 1, 1, tzinfo=timezone(settings.TZ))
    end_date = datetime(2025, 4, 30, tzinfo=timezone(settings.TZ))

    with Imbox(**get_credentials(credentials=credentials)) as imbox:
        # Buscar e-mails a partir de uma data específica
        messages = imbox.messages(unread=True, date__gt=start_date, date__lt=end_date)
        logger.debug(ic(f'{len(messages)=}'))
        for atual in messages[:]:
            uid, email = atual
            print(f'TITULO DO EMAIL: {email.subject}')
            print(f'DATA DO EMAIL: {email.date}')
            print(f'Remetente: {email.sent_from}')

            imbox.mark_seen(uid)   # Marcar as mensagens como lidos

def get_email_11(credentials: Path | None = None, **kwargs) -> None:
    """Get the email from the credentials.json file.

    Consulta e marca mensagens como lidas a partir de um parametro especificado.
    """
    credentials = credentials or CREDENTIALS_PATH

    start_date = datetime(2021, 1, 1, tzinfo=timezone(settings.TZ))
    end_date = datetime(2025, 4, 30, tzinfo=timezone(settings.TZ))

    with Imbox(**get_credentials(credentials=credentials)) as imbox:
        # Todas as mensagens
        all_messages = imbox.messages(**kwargs)
        logger.info(ic(f'{len(all_messages)=}'))

        # Messages RECEBIDAS DE
        imbox_messages_de = imbox.messages(sent_from='noreply@github.com', unread=True)
        logger.info(ic(f'{imbox_messages_de=}'))

        # Messages ENVIADAS PARA
        imbox_messages_para = imbox.messages(sent_to='dev@incolume.com.br')
        logger.info(ic(f'{imbox_messages_para=}'))

        # Datas específicas
        inbox_antes = imbox.messages(date__lt=dt.datetime.now())
        logger.info(ic(f'{inbox_antes=}'))

        inbox_depois = imbox.messages(date__gt=dt.date(2021, 1, 1))
        logger.info(ic(f'{inbox_depois=}'))

        # Data exata
        inbox_data_exata = imbox.messages(date__on=dt.date(2021, 1, 1))
        logger.info(ic(f'{inbox_data_exata=}'))

        # Mensagens que contenham uma string
        messages_string = imbox.messages(subject='Tempmail')
        logger.info(ic(f'{messages_string=}'))

        # Mensagens de uma pasta específica
        messages_pasta_x = imbox.messages(folder='Spam')
        logger.info(ic(f'{messages_pasta_x=}'))


class RPAEmail:
    """Robotic Process Automation Email.

    Classe para automação de processos robóticos com email.
    Atributos:
        credentials (Path | None): Caminho para o arquivo de credenciais.
        hostname (str): Nome do host do servidor de email.
        attachments (str): Pasta para anexos.
        filtrados (str): Pasta para emails filtrados.
        pasta (str): Pasta de emails.
    """

    def __init__(self, credentials: Path | None = None, hostname: str = ''):
        """_summary_

        Args:
            credentials (Path | None, optional): _description_. Defaults to None.
        """
        with credentials.open() as file:
            credentials_data = json.load(file)

        self.credentials = credentials or CREDENTIALS_PATH
        self.hostname = hostname or IMAP_SERVER
        self.email = credentials_data['email']
        self.__password = credentials_data['google_password']

        self.attachments = 'attachements'
        self.filtrados = 'filtrados'
        self.pasta = 'pasta'



def run():
    """Run the script."""
    """
    get_email_0()
    get_email_1()
    get_email_2()
    get_email_3()
    get_email_4()
    get_email_5()
    get_email_8()
    get_email_9()
    get_email_10()
    get_email_11()
    """


if __name__ == '__main__':
    run()
