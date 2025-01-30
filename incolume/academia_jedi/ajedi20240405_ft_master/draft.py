"""Module."""

from flet import (
    Column,
    Container,
    CrossAxisAlignment,
    MainAxisAlignment,
    Row,
    UserControl,
    VerticalDivider,
)

# ruff: noqa: T201


class ClassName(UserControl):
    """Class."""

    def __init__(self, route):
        """Init it."""
        super().__init__()
        self.route = route

    def build(self):
        """Build it."""
        page_content = Container(
            padding=0,
            border_radius=5,
            expand=True,
            content=Column(
                controls=[
                    # main body
                    Container(
                        expand=True,
                        content=Row(
                            vertical_alignment=CrossAxisAlignment.START,
                            controls=[
                                Container(
                                    expand=5,
                                    border_radius=5,
                                    padding=15,
                                    # content=
                                    #
                                    # Insert controls here
                                    #
                                ),
                                VerticalDivider(width=1),
                                Container(
                                    expand=2,
                                    border_radius=5,
                                    padding=15,
                                    content=Column(
                                        alignment=MainAxisAlignment.START,
                                        horizontal_alignment=CrossAxisAlignment.CENTER,
                                        spacing=20,
                                        controls=[
                                            #
                                            # Insert controls here
                                            #
                                        ],
                                    ),
                                ),
                            ],
                        ),
                    ),
                ],
            ),
        )

        return Row(
            expand=True,
            spacing=10,
            controls=[
                page_content,
            ],
        )

    def initialize(self):
        """Init it."""
        print("Initializing 'YourClassName'")
        # Implement initializing of the page here
