"""In this section, we will learn about the functionality.

 of Flet Checkbox control.

Note:
Flet provides a number of controls for building forms:
TextField, Checkbox, Dropdown, ElevatedButton, etc.
"""

# let's build a simple to-do app
from logging import info

import flet as ft


def main(page: ft.Page) -> None:
    """Main."""

    def checkbox_change(e: ft.ControlEvent) -> None:
        output_text.value = (
            f"You have learned Swimming, that's great: {todo_check.value}"
        )
        info('%s', e)
        page.update()

    todo_check = ft.Checkbox(
        label='Learn Swimming',
        value=False,
        on_change=checkbox_change,
    )
    output_text = ft.Text()

    page.add(
        todo_check,
        output_text,
    )


if __name__ == '__main__':  # pragma: no cover
    ft.app(target=main)
