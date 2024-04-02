"""User Control."""

import flet as ft

"""
Theory: Why do we need User Controls

1) UserControl allows building isolated re-usable components
    by combining existing Flet Controls.

2) UserControl must implement build() that is called
    to build the control's UI.

3) build() function should return a single Control
    instance of a List of controls.
"""


class GreeterControl(ft.UserControl):
    """Greeter Control."""

    def build(self):
        """Build."""
        return ft.Row(
            [ft.Text('Hello World!'), ft.ElevatedButton('I am a button')],
            alignment='center',
        )


def main(page: ft.Page) -> None:
    """Main."""
    page.add(GreeterControl())


if __name__ == '__main__':  # pragma: no cover
    ft.app(target=main)
