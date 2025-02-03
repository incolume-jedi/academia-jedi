"""Acesso a gsheet.


Codificação oriunda de
http://github.com/incolumepy-prospections/incolumepy.dataclass.
"""

import logging
from collections.abc import Iterator
from itertools import chain
from pathlib import Path

import gspread
from oauth2client.service_account import ServiceAccountCredentials

__author__ = '@britodfbr'  # pragma: no cover

# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293


class GSheet:
    """GSheet access."""

    def __init__(
        self,
        credentials: Path | None = None,
        escopo: Iterator | None = None,
    ):
        """"""
        self.credentials: Path = credentials
        self.escopo: Iterator = escopo

    @property
    def credentials(self) -> Path:
        """Autenticação API Google."""
        return self.__credential

    @credentials.setter
    def credentials(self, file_credential: Path = None) -> None:
        """Autenticação API Google."""
        logging.info('setting: %s', file_credential)
        if not file_credential:
            logging.debug('not file: %s', file_credential)
            file_credential = (
                Path('~')
                .expanduser()
                .joinpath(
                    'projetos',
                    'private',
                    'authkeys',
                    'incolumepy-dev-6ae65605985c.json',
                )
            )
            logging.info('setting: %s', file_credential)
        if not file_credential.is_file():
            logging.debug('not file: %s', file_credential)
            file_credential = (
                Path(__file__)
                .parents[0]
                .joinpath(
                    'credentials',
                    'incolumepy-dev-6ae65605985c.json',
                )
            )
            logging.info('setting: %s', file_credential)
        logging.debug('return: %s', file_credential)
        file_credential.read_bytes()
        self.__credential = file_credential

    @property
    def escopo(self):
        """Escope to gsheet."""
        return self.__escopo

    @escopo.setter
    def escopo(self, value: list[str] = None) -> None:
        """Escope to gsheet."""
        value = value or []
        self.__escopo = chain(
            [
                'https://spreadsheets.google.com/feeds',
                'https://www.googleapis.com/auth/drive',
            ],
            value,
        )

    @property
    def client_google(self):
        credenciais = ServiceAccountCredentials.from_json_keyfile_name(
            self.credentials,
            self.escopo,
        )

        # client_google
        gc = gspread.authorize(credenciais)
        return gc

    def drop_sheet(self, spreadsheet, dropthis: bool = False) -> bool:
        """Drop Planilha

        :param spreadsheet:
        :param dropthis: bool
        :return: bool
        """
        if dropthis:
            self.client_google.del_spreadsheet(spreadsheet.id)
            return True
        return False

    def load_create_sheet(self, spreadsheetname):
        """Carregar/Criar Planilha.

        :return:
        """
        try:
            spreadsheet = self.client_google.open(spreadsheetname)
        except (
            gspread.exceptions.SpreadsheetNotFound,
            gspread.exceptions.APIError,
        ):
            spreadsheet = self.client_google.create(spreadsheetname)

        return spreadsheet

    def permission_sheet(self, spreadsheet, users: list[str]):
        """permissões Planilha.

        :param spreadsheet:
        :param users: list[str] lista com email de usuários
        :return:
        """
        list_users = chain(
            [
                'brito@incolume.com.br',
                'britodfbr@gmail.com',
                'dev@incolume.com.br',
                'dataaccess@incolumepy-dev.iam.gserviceaccount.com',
            ],
            users,
        )
        for user in list_users:
            logging.info(user)
            spreadsheet.share(user, perm_type='user', role='writer')

    def get_url_sheet(self, spreadsheet):
        """Link acesso web

        :return:
        """
        result = f'https://docs.google.com/spreadsheets/d/{spreadsheet.id}'
        logging.debug(result)
        return result
