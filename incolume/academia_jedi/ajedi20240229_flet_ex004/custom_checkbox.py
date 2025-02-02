"""Custom CheckBox."""

# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293

from logging import debug, info

import flet as ft


class CustomCheckBox(ft.UserControl):
    """Custom CheckBox."""

    def __init__(
        self,
        *args,
        **kwargs,
    ):
        """Init.

        color,
        label='',
        selection_fill='#183588',
        size=25,
        stroke_width=2,
        animation=None,
        checked=bool,
        font_size=17,
        pressed=None,
        """
        super().__init__(*args, **kwargs)
        # self.selection_fill = selection_fill
        # self.color = color
        # self.label = label
        # self.size = size
        # self.stroke_width = stroke_width
        # self.animation = animation
        # self.checked = checked
        # self.font_size = font_size
        # self.pressed = pressed

    def _checked(self):
        self.check_box = ft.Container(
            animate=self.animation,
            width=self.size,
            height=self.size,
            border_radius=(self.size / 2) + 5,
            bgcolor=self.CHECKED,
            content=ft.Icon(
                ft.icons.CHECK_ROUNDED,
                size=15,
            ),
        )
        return self.check_box

    def _unchecked(self):
        self.check_box = ft.Container(
            animate=self.animation,
            width=self.size,
            height=self.size,
            border_radius=(self.size / 2) + 5,
            bgcolor=None,
            border=ft.border.all(color=self.color, width=self.stroke_width),
            content=ft.Container(),
        )
        return self.check_box

    def build(self):
        """Build It."""
        self.BG = '#041955'
        self.FG = '#3450a1'
        self.PINK = '#eb06ff'
        self.CHECKED = '#183588'

        if self.checked is True:
            return ft.Column(
                controls=[
                    ft.Container(
                        on_click=lambda e: self.checked_check(e),
                        content=ft.Row(
                            controls=[
                                self._checked(),
                                ft.Text(
                                    self.label,
                                    font_family='poppins',
                                    size=self.font_size,
                                    weight=ft.FontWeight.W_300,
                                ),
                            ],
                        ),
                    ),
                ],
            )

        return ft.Column(
            controls=[
                ft.Container(
                    on_click=lambda e: self.checked_check(e),
                    content=ft.Row(
                        controls=[
                            self._unchecked(),
                            ft.Text(
                                self.label,
                                font_family='poppins',
                                size=self.font_size,
                                weight=ft.FontWeight.W_300,
                            ),
                        ],
                    ),
                ),
            ],
        )

    def checked_check(self, e):
        """Checked Check."""
        info('Event: %s', e)
        debug(self.checked)
        if self.checked is False:
            self.checked = True
            self.check_box.border = None
            self.check_box.bgcolor = self.CHECKED
            self.check_box.content = ft.Icon(
                ft.icons.CHECK_ROUNDED,
                size=15,
            )
            self.update()

        elif self.checked is True:
            self.checked = False
            self.check_box.bgcolor = None
            self.check_box.border = ft.border.all(
                color=self.color,
                width=self.stroke_width,
            )
            self.check_box.content.visible = False
            self.update()

        if self.pressed:
            self.run()

    def is_checked(self):
        """Checked."""
        return self.checked

    def run(self, *args):
        """Run."""
        self.pressed(args)
