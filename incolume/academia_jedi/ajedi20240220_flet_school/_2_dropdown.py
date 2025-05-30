"""In this section, we will learn about Flet Dropdown Control."""

from logging import info

import flet as ft


def main(page: ft.Page) -> None:
    """Main."""
    page.title = 'Color Drodown'
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'

    def btn_click(e: ft.ControlEvent) -> None:
        print_output.value = f'You have selected => {color_dropdown.value}'
        info('%s', e)
        page.update()

    color_dropdown = ft.Dropdown(
        width=300,
        options=[
            ft.dropdown.Option('Red'),
            ft.dropdown.Option('Green'),
            ft.dropdown.Option('Blue'),
        ],
    )

    button = ft.ElevatedButton(text='Submit', on_click=btn_click)
    print_output = ft.Text()

    page.add(
        color_dropdown,
        button,
        print_output,
    )


if __name__ == '__main__':  # pragma: no cover
    ft.app(target=main)

"""
NOTE:

If you don't select anything from Dropdown and click on Submit button,
it will print None.
"""
