"""Module."""

from flet import (
    AlertDialog,
    MainAxisAlignment,
    RoundedRectangleBorder,
    Text,
    TextButton,
)

# ruff: noqa: A002, ANN001, ANN201, ARG002, BLE001, C901, D101, D102, D107, DTZ005, DTZ011, E501, ERA001, N802, N803, N806, PLR2004, S608, T201, TRY300


class ConfirmDialog(AlertDialog):
    """Creates an AlertDialog that, if "yes" clicked, executes the function passed as a parameter.

    Args:
        function (method): method to be executed
        title (string): title of the dialog
        content (string): content of the question to be confirmed
    """

    def __init__(self, function, title='', content=''):
        super().__init__()
        self.function = function

        self.modal = True
        self.title = Text(title)
        self.content = Text(content)
        self.actions = [
            TextButton('Não', on_click=self.canceled),
            TextButton(
                content=Text('Sim', color='red'),
                on_click=self.confirmed,
            ),
        ]
        self.actions_alignment = MainAxisAlignment.END
        self.shape = RoundedRectangleBorder(radius=10)

    def build(self):
        return self

    def confirmed(self, e):
        self.open = False
        self.update()
        self.function(self.data)

    def canceled(self, e):
        self.open = False
        self.update()
