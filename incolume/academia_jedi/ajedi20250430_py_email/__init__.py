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
SMTP_SERVER: Final[str] = 'smtp.google.com'
IMAP_SERVER: Final[str] = 'imap.google.com'

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

    return {
        'hostname': IMAP_SERVER,
        'username': credentials_data['email'],
        'password': credentials_data['google_password'],
    }


def get_email(credentials: Path | None = None) -> Email:
    """Get the email from the credentials.json file."""
    with Imbox(**get_credentials(credentials)) as inbox:
        unread_messages = inbox.messages(unread=True)  # Get unread messages
        if not unread_messages:
            logger.info(ic('No unread messages'))
        print(len(unread_messages))



if __name__ == '__main__':
    get_email()
