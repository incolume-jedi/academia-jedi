"""MOdule."""

# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293

from datetime import date

import bcrypt
from Database import UserDatabase
from flet import (
    AlertDialog,
    Column,
    OutlinedButton,
    Row,
    Text,
    TextAlign,
    TextField,
    icons,
)
from Notification import Notification

# ruff: noqa: A002, ANN001, ANN201, ARG002, BLE001, C901, D101, D102, D107, DTZ005, DTZ011, E501, ERA001, N802, N803, N806, PLR2004, S608, T201, TRY300


class CreateFirstAdmin(AlertDialog):
    def __init__(self, route):
        super().__init__()
        self.route = route

        self.modal = True
        self.title = Row(
            expand=True,
            alignment='center',
            controls=[
                Text(
                    value='Cadastro do administrador',
                    text_align=TextAlign.CENTER,
                    width=350,
                ),
            ],
        )

        self.tf_name = TextField(
            autofocus=True,
            label='Nome',
            prefix_icon=icons.PERSON_2_ROUNDED,
            on_change=self.validate_fields,
        )
        self.tf_user = TextField(
            label='Usuário',
            prefix_icon=icons.ASSIGNMENT_IND_ROUNDED,
            on_change=self.validate_fields,
        )
        self.tf_pass1 = TextField(
            label='Insira a senha',
            password=True,
            prefix_icon=icons.PASSWORD,
            on_change=self.validate_fields,
        )
        self.tf_pass2 = TextField(
            label='Repita a senha',
            password=True,
            prefix_icon=icons.PASSWORD,
            on_change=self.validate_fields,
        )
        self.btn_register_user = OutlinedButton(
            text='Cadastrar',
            disabled=True,
            icon=icons.ADD_OUTLINED,
            width=140,
            on_click=self.register_admin,
        )

        self.actions = [
            Column(
                expand=True,
                horizontal_alignment='center',
                controls=[
                    self.tf_name,
                    self.tf_user,
                    self.tf_pass1,
                    self.tf_pass2,
                    self.btn_register_user,
                ],
            ),
        ]

    def build(self):
        return self

    def validate_fields(self, e):
        required_fields = [
            self.tf_name,
            self.tf_user,
            self.tf_pass1,
            self.tf_pass2,
        ]
        all_filled = all(control.value != '' for control in required_fields)
        all_empty = all(control.value == '' for control in required_fields)

        if all_empty:
            for control in required_fields:
                control.error_text = ''
            self.btn_register_user.disabled = True
            self.update()
            return

        if all_filled:
            if self.tf_pass1.value != self.tf_pass2.value:
                self.tf_pass1.error_text = 'Senhas não conferem!'
                self.tf_pass2.error_text = 'Senhas não conferem!'
                self.btn_register_user.disabled = True
                self.update()
                return
            for control in required_fields:
                control.error_text = ''
            self.btn_register_user.disabled = False
            self.update()
            return

        for control in required_fields:
            if control.value == '':
                control.error_text = 'Campos Obrigatórios!'
                control.update()
            self.btn_register_user.disabled = True
            self.update()

    def create_hash(self, password):
        salt = bcrypt.gensalt()
        hashed_pass = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_pass.decode('utf-8')

    def prepare_data(self):
        today = date.today()
        form_date = today.strftime('%Y-%m-%d')
        hashed_pass = self.create_hash(self.tf_pass1.value)
        return [
            self.tf_name.value,
            self.tf_user.value,
            hashed_pass,
            form_date,
            'Admin',
        ]

    def register_admin(self, e):
        fulldataset = self.prepare_data()
        mydb = UserDatabase(self.route)
        mydb.connect()
        result = mydb.register_user(fulldataset)
        mydb.close()

        if result == 'success':
            Notification(
                self.route.page,
                'Administrador cadastrado com sucesso!',
                'green',
            ).show_message()
            self.open = False
        else:
            Notification(
                self.route.page,
                f'Erro ao cadastrar o administrador: {result}',
                'red',
            ).show_message()

        self.route.page.update()
