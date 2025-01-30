"""Module."""

from flet import (
    DismissDirection,
    SnackBar,
    SnackBarBehavior,
    Text,
    TextThemeStyle,
    UserControl,
)

# ruff: noqa: ARG002 A002 DTZ011 C901 T201 ANN001 ANN201 ERA001 D101 D102 D107 E501 PLR2004 BLE001 DTZ005 N802


class Notification(UserControl):
    def __init__(self, page, message, color):
        super().__init__()
        self.page = page
        self.message = message
        self.color = color
        self.content = Text(
            value=message,
            color=color,
            style=TextThemeStyle.BODY_LARGE,
        )
        self.snack_bar = SnackBar(
            content=self.content,
            elevation=10,
            duration=6000,
            show_close_icon=True,
            behavior=SnackBarBehavior.FLOATING,
            dismiss_direction=DismissDirection.END_TO_START,
        )

    def show_message(self):
        self.page.snack_bar = self.snack_bar
        self.snack_bar.open = True
        self.page.update()
