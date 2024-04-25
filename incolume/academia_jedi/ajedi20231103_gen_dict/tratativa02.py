"""Codificação oriunda de http://github.com/incolumepy-prospections/incolumepy.dataclass."""

import logging
from pathlib import Path
import gspread
from oauth2client.service_account import ServiceAccountCredentials

__author__ = '@britodfbr'  # pragma: no cover


def set_credentials(file_credencial: Path = None) -> Path:
    """Autenticação API Google."""
    logging.info('setting: %s', file_credencial)
    if file_credencial is None or not file_credencial.is_file():
        logging.debug('not file: %s', file_credencial)
        file_credencial = (
            Path(__file__)
            .parents[0]
            .joinpath(
                'credentials',
                'incolumepy-dev-6ae65605985c.json',
            )
        )
        logging.info('setting: %s', file_credencial)
    if not file_credencial.is_file():
        logging.debug('not file: %s', file_credencial)
        file_credencial = (
            Path('~')
            .expanduser()
            .joinpath(
                'projetos',
                'private',
                'authkeys',
                'incolumepy-dev-6ae65605985c.json',
            )
        )
        logging.info('setting: %s', file_credencial)
    logging.debug('return: %s', file_credencial)
    return file_credencial


def get_client_google(crendential_file=''):
    crendential_file = crendential_file or set_credentials().as_posix()
    escopo = [
        'https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive',
    ]
    credenciais = ServiceAccountCredentials.from_json_keyfile_name(
        crendential_file, escopo
    )

    # client_google
    gc = gspread.authorize(credenciais)
    return gc


def drop_sheet(spreadsheet, dropthis: bool = False):
    """Drop Planilha

    :param spreadsheet:
    :param dropthis:
    :return:
    """
    if dropthis:
        gc = get_client_google()
        gc.del_spreadsheet(spreadsheet.id)
        return True
    return False


def load_create_sheet(spreadsheetname):
    """Carregar/Criar Planilha.

    :return:
    """
    gc = get_client_google()
    try:
        spreadsheet = gc.open(spreadsheetname)
    except (
        gspread.exceptions.SpreadsheetNotFound,
        gspread.exceptions.APIError,
    ):
        spreadsheet = gc.create(spreadsheetname)

    return spreadsheet


def permission_sheet(spreadsheet):
    """permissões Planilha.

    :param spreadsheet:
    :return:
    """
    users = [
        'brito@incolume.com.br',
        'britodfbr@gmail.com',
        'dev@incolume.com.br',
        'dataaccess@incolumepy-dev.iam.gserviceaccount.com',
    ]
    for user in users:
        spreadsheet.share(user, perm_type='user', role='writer')


def get_url_sheet(spreadsheet):
    """Link acesso web

    :return:
    """
    result = f'https://docs.google.com/spreadsheets/d/{spreadsheet.id}'
    return result
