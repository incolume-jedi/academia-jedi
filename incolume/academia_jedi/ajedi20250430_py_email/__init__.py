"""Email with python."""

import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Final

from icecream import ic
from imbox import Imbox
from incolume.academia_jedi import logger

CREDENTIALS_PATH: Final[Path] = (
    Path(__file__).parents[3] / 'credentials' / 'credentials.json'
)
SMTP_SERVER: Final[str] = 'smtp.gmail.com'
IMAP_SERVER: Final[str] = 'imap.gmail.com'

logger.info(ic(f'{CREDENTIALS_PATH=}, {SMTP_SERVER=}, {IMAP_SERVER=}'))


@dataclass
class Email:
    """Email class."""

    username: str
    password: str
    hostname: str = 'imap.gmail.com'


def get_credentials(credentials: Path | None = None):
    """Get the credentials from the credentials.json file."""
    credentials = credentials or CREDENTIALS_PATH
    logger.debug(ic(f'{credentials=}'))
    with credentials.open() as file:
        credentials_data = json.load(file)

    logger.debug(ic(f'{credentials_data=}'))
    return {
        'hostname': 'imap.google.com',
        'username': credentials_data['email'],
        'password': credentials_data['google_password'],
    }


# with Imbox(**get_credentials()) as inbox:
#    # Get unread messages
#    unread_messages = inbox.messages(unread=True)
#
#    print(len(unread_messages))
#    # for uid, message in unread_messages:
#    #     print(f'From: {message.sent_from}')
#    #     print(f'Subject: {message.subject}')
#    #     print(f'Date: {message.date_str}')
#    #     print(f"Body: {message.body['plain']}")
#    #     print('-' * 40)
