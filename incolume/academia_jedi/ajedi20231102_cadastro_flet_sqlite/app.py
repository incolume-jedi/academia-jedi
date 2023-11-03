"""APP Module."""

from dotenv import load_dotenv
from flet import (
    Card,
    Column,
    Container,
    ElevatedButton,
    IconButton,
    Page,
    Radio,
    RadioGroup,
    Row,
    SnackBar,
    Text,
    TextField,
    animation,
    transform,
)

from incolume.academia_jedi.\
    ajedi20231102_cadastro_flet_sqlite.database import (
    create_table,
    get_connection,
)

import logging

__author__ = '@britodfbr'  # pragma: no cover

load_dotenv()


def main(page: Page) -> None:
    """Main func."""
    create_table()
    page.scroll = 'auto'

    def showinput(*args) -> None:
        """Showinput."""
        inputcont.offset = transform.Offset(0, 0)
        page.update()

    def hidecon(*args) -> None:
        """Showinput."""
        inputcont.offset = transform.Offset(0, 0)
        page.update()

    def save_data(*args) -> None:
        """Save data."""
        try:
            conn = get_connection()
            c = conn.cursor()
            c.execute(
                'INSERT INTO users (name,age,contact,email,address,'
                'gender) VALUES (?,?,?,?,?,?)',
            )
            conn.commit()
            logging.debug('write db success.')
        except Exception as err:
            logging.error('%s' % err)
            # raise err
            inputcont.offset = transform.Offset(2, 0)
            page.snack_bar = SnackBar(
                Text('success'),
                bgcolor='green',
            )
            page.snack_bar.open = True
            page.update()

    name = TextField(label='name')
    contact = TextField(label='contact')
    age = TextField(label='age')
    gender = TextField(label='gender')
    email = TextField(label='email')
    address = TextField(label='address')

    inputcont = Card(
        offset=transform.Offset(2, 0),
        animate_offset=animation.Animation(600, curve='easeIn'),
        elevation=30,
        content=Container(
            [
                Row(
                    [
                        Text('add dados', size=20, weight='bold'),
                        IconButton(
                            icon='Sair', icon_size=30, on_click=hidecon,
                        ),
                    ],
                ),
            ],
        ),
    )

    page.add(
        Column(
            [
                Text('cadastro de usuários', size=30, weight='bold'),
                ElevatedButton('Cadastrar', on_click=showinput),
            ],
        ),
    )
