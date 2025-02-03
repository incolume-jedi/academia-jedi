"""Module."""

# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293

from CreateFirstAdmin import CreateFirstAdmin
from Database import UserDatabase
from flet import (
    BoxShadow,
    Column,
    Container,
    CrossAxisAlignment,
    MainAxisAlignment,
    Offset,
    OutlinedButton,
    Row,
    ShadowBlurStyle,
    Text,
    TextField,
    TextThemeStyle,
    UserControl,
    alignment,
    colors,
    icons,
    padding,
)
from Notification import Notification

# ruff: noqa: ARG002 A002 DTZ011 C901 T201 ANN001 ANN201 ERA001 D101 D102 D107 E501 PLR2004 BLE001 DTZ005 N802


class Login(UserControl):
    def __init__(self, route):
        super().__init__()
        self.route = route

    def build(self):
        self.text_user = TextField(
            label='Usuário',
            prefix_icon=icons.PERSON_2_OUTLINED,
            expand=True,
            autofocus=True,
            on_change=self.analyze_to_enable_button,
        )
        self.text_password = TextField(
            label='Senha',
            prefix_icon=icons.LOCK_OUTLINE_ROUNDED,
            expand=True,
            password=True,
            can_reveal_password=True,
            on_change=self.analyze_to_enable_button,
        )
        self.btn_login = OutlinedButton(
            text='Login',
            width=240,
            icon=icons.LOGIN_OUTLINED,
            disabled=True,
            on_click=self.login_clicked,
        )
        return Container(
            # bgcolor='black',
            expand=True,
            alignment=alignment.center,
            content=Row(
                expand=True,
                alignment=MainAxisAlignment.CENTER,
                vertical_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    Container(
                        padding=padding.only(60, 34, 60, 20),
                        bgcolor=colors.SURFACE,
                        border_radius=10,
                        width=500,
                        height=360,
                        shadow=BoxShadow(
                            spread_radius=5,
                            blur_radius=5,
                            color=colors.GREY_300,
                            offset=Offset(1, 1),
                            blur_style=ShadowBlurStyle.NORMAL,
                        ),
                        content=Column(
                            # expand=True,
                            spacing=30,
                            alignment=MainAxisAlignment.START,
                            horizontal_alignment=CrossAxisAlignment.CENTER,
                            tight=True,
                            controls=[
                                Row(
                                    alignment=MainAxisAlignment.CENTER,
                                    controls=[
                                        Text(
                                            'Login',
                                            style=TextThemeStyle.TITLE_LARGE,
                                        ),
                                    ],
                                ),
                                Row(
                                    controls=[
                                        self.text_user,
                                    ],
                                ),
                                Row(
                                    controls=[
                                        self.text_password,
                                    ],
                                ),
                                Row(
                                    alignment=MainAxisAlignment.CENTER,
                                    controls=[
                                        self.btn_login,
                                    ],
                                ),
                            ],
                        ),
                    ),
                ],
            ),
        )

    def initialize(self):
        if not self.route.bar.scheduler.running:
            self.route.bar.scheduler.start()

    def verify_count_of_users(self):
        mydb = UserDatabase(self.route)
        mydb.connect()
        result = mydb.select_users_count()
        mydb.close()
        return result != '0'

    def create_admin(self):
        dialog = CreateFirstAdmin(self.route)
        self.route.page.dialog = dialog
        dialog.open = True
        self.route.page.update()

    def go_to_home(self, name, permission):
        self.route.config.set_permissions(name, permission)

        self.page.go('/home')
        self.route.bar.enable_btn_logout()
        self.route.bar.set_username(name)
        self.route.bar.set_title('Página Inicial')
        self.route.menu.cont.visible = True
        self.route.menu.update()
        self.route.page.update()

    def login(self):
        data = [self.text_user.value, self.text_password.value]
        mydb = UserDatabase(self.route)
        mydb.connect()
        name, permission = mydb.login_verify(data)
        mydb.close()

        if name is None:
            Notification(
                self.page,
                'Usuário ou senha incorretos!',
                'red',
            ).show_message()
            return
        self.go_to_home(name, permission)

    def login_clicked(self, e):
        self.route.config.initialize()

        if self.route.config.host is None:
            return

        if not self.verify_count_of_users():
            self.create_admin()
            return

        self.login()

    def analyze_to_enable_button(self, e):
        self.btn_login.disabled = (
            self.text_user.value == '' or self.text_password.value == ''
        )
        self.update()
