"""Module."""

# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293

import json

import mysql.connector
from cryptography.fernet import Fernet
from flet import (
    AlertDialog,
    Column,
    MainAxisAlignment,
    Row,
    Text,
    TextButton,
    TextField,
)
from Notification import Notification

# ruff: noqa: A002, ANN001, ANN201, ARG002, BLE001, C901, D101, D102, D107, DTZ005, DTZ011, E501, ERA001, N802, N803, N806, PLR2004, S608, T201, TRY300


class CreateConfig(AlertDialog):
    def __init__(self, route):
        super().__init__()
        self.route = route
        self.modal = True
        self.title = Row(
            expand=True,
            controls=[
                Text('Configurar conexão ao banco de dados:', width=500),
            ],
        )

        self.tf_host = TextField(label='Host', value='localhost')
        self.tf_user = TextField(label='User', value='root')
        self.tf_passwd = TextField(label='Password', value='')
        self.tf_database = TextField(label='Database', value='')
        self.tf_port = TextField(label='Port', value='3306')
        self.btn_back = TextButton(text='Voltar', on_click=self.back_clicked)
        self.btn_save = TextButton(text='Salvar', on_click=self.save_bd_config)

        self.actions = [
            Column(
                width=500,
                expand=True,
                controls=[
                    self.tf_host,
                    self.tf_user,
                    self.tf_passwd,
                    self.tf_database,
                    self.tf_port,
                    Row(
                        alignment=MainAxisAlignment.END,
                        controls=[self.btn_back, self.btn_save],
                    ),
                ],
            ),
        ]

    def build(self):
        return self

    def back_clicked(self, e):
        self.open = False
        self.route.page.update()

    def generate_key(self):
        return Fernet.generate_key()

    def encrypt_data(self, data, key):
        fernet = Fernet(key)
        return fernet.encrypt(data.encode())

    def write_file(self, key, encrypted_data):
        try:
            with open('data.bin', 'wb') as file:
                file.write(key)
                file.write(b'\n')
                file.write(encrypted_data)
            Notification(
                self.route.page,
                'Configuração realizada com sucesso!',
                'green',
            ).show_message()
        except Exception as e:
            Notification(
                self.route.page,
                f'Erro ao salvar a conexão. Tente reiniciar o sistema! {e}',
                'red',
            ).show_message()

    def test_connection(self, config_dict):
        config = json.loads(config_dict)
        try:
            connection = mysql.connector.connect(
                host=config['host'],
                user=config['user'],
                passwd=config['passwd'],
                database=config['database'],
                port=config['port'],
            )
            connection.close()
            return True
        except Exception as e:
            Notification(
                self.route.page,
                f'Erro ao criar a conexão. Verifique os dados inseridos! {e}',
                'red',
            ).show_message()
            return False

    def save_bd_config(self, e):
        config_dict = f"""
            {
            {
                'host': '{self.tf_host.value}',
                'user': '{self.tf_user.value}',
                'passwd': '{self.tf_passwd.value}',
                'database': '{self.tf_database.value}',
                'port': '{self.tf_port.value}',
            }
        }
        """
        if self.test_connection(config_dict):
            key = self.generate_key()
            encrypted_data = self.encrypt_data(config_dict, key)
            self.write_file(key, encrypted_data)
            self.back_clicked(e)
