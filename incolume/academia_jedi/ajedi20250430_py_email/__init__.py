"""Email with python."""

import json
import pprint
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
        for uid, message in messages[-1]:
            print(message.sent_from, message.subject)


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



def get_email_4(credentials: Path | None = None) -> str:
    """Get the email from the credentials.json file."""

    timestamp = '2010-01-01'

    with Imbox(**get_credentials(credentials)) as inbox:
        messages = inbox.messages(date__on=timestamp)
        for msg in messages:
            msg.delete()

def run():
    """Run the script."""
    get_email_0()
    get_email_1()
    get_email_2()
    get_email_3()
    get_email_4()


if __name__ == '__main__':
    run()
