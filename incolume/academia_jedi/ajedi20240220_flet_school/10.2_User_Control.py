"""User Control."""

from logging import info

import flet as ft

"""
Theory:

1) UserControl should call self.update() to push its
    changes to a Flet page.

2) super().__init__() must be always
    called in your own constructor.
"""


class Counter(ft.UserControl):
    """Counter."""

    def __init__(self, initial_count):
        """Init."""
        super().__init__()
        self.counter = initial_count

    def add_click(self, e):
        """Click."""
        info('Event: %s', e)
        self.counter += 1
        self.text.value = str(self.counter)
        self.update()

    def build(self):
        """Build."""
        self.text = ft.Text(str(self.counter))
        return ft.Row([
            self.text,
            ft.ElevatedButton('Add', on_click=self.add_click),
        ])


def main(page: ft.Page) -> None:
    """Main."""
    page.add(Counter(100), Counter(45))


if __name__ == '__main__':  # pragma: no cover
    ft.app(target=main)
