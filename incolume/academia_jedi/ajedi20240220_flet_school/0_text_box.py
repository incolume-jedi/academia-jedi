"""In this section, we will learn about the functionality of Flet Textbox.

So, let's build a simple app which can say hello to a person.
access in:
https://github.com/kmranrg/FletSchool/blob/main/03_GettingUserInput/Part_01/2_TextBox.py.
"""

import flet as ft
from logging import info


def main(page: ft.Page) -> None:
    """Main."""
    page.title = 'Say Hello!'
    page.horizontal_alignment = 'center'
    page.padding = 100

    user_name = ft.TextField(label='Enter name', width=300)
    print_name_column = ft.Column()

    def call_hello(e: ft.ControlEvent) -> None:
        if not user_name.value:
            user_name.error_text = 'You forgot to enter the name!'
            page.update()
        else:
            page.clean()
            print_name_column.controls.append(
                ft.Text(f'Hello, {user_name.value}!'),
            )
            info('%s', e)
            page.add(print_name_column)

    page.add(
        user_name,
        ft.ElevatedButton('Say Hello!', on_click=call_hello),
        print_name_column,
    )


if __name__ == '__main__':  # pragma: no cover
    ft.app(target=main)
