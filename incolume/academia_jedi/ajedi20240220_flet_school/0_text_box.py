"""In this section, we will learn about the functionality of Flet Textbox.

# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293

So, let's build a simple app which can say hello to a person.
access in:
https://github.com/kmranrg/FletSchool/blob/main/03_GettingUserInput/Part_01/2_TextBox.py.
"""

from logging import info

import flet as ft


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
