"""Exemplo validação de campo."""

import logging

import flet as ft


def main(page: ft.Page) -> None:
    """Run it."""

    def submit(e: ft.ControlEvent) -> None:
        logging.debug(e)
        page.add(ft.Text(f'Your phone number is: {field.value}'))

    field = ft.TextField(
        label='Enter your PhoneNumber:',
        suffix=ft.ElevatedButton('Submit', on_click=submit),
        keyboard_type=ft.KeyboardType.NUMBER,
        on_submit=submit,
        input_filter=ft.InputFilter(
            allow=True,
            regex_string=r'[0-9+]',
            replacement_string='',
        ),
    )

    page.add(field)


if __name__ == '__main__':  # pragma: no cover
    ft.app(target=main)
