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
    """
    get_email_8()


if __name__ == '__main__':
    run()
