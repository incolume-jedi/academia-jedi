"""Email with python."""

from email.message import EmailMessage
import smtplib
import ssl
import os
import mimetypes
from pathlib import Path
from config import settings
from icecream import ic
from incolume.academia_jedi import logger
import json
from incolume.academia_jedi.ajedi20250430_py_email import CREDENTIALS_PATH


__all__ = ['EmailMessage', 'smtplib', 'ssl', 'os', 'mimetypes', 'Path']

with Path(__file__).parents[3].joinpath('credentials','credentials.json').open() as f:
    data = json.load(f)
    remetente = data['email']
    senha = data['google_password']

logger.info(ic(f'senha: {senha}'))
logger.info(ic(f'Remetente: {remetente}'))

destinatarios: list[str] = ['jesoxid995@benznoi.com', 'britodfbr@gmail.com']
logger.info(ic(f'Destinatários: {destinatarios}'))
assunto = 'Relatório mensal'
logger.info(ic(f'Assunto: {assunto}'))
body = Path(__file__).parent.joinpath('content_txt.txt').read_text()
logger.info(ic(f'Conteúdo do email: {body}'))

mensagem = EmailMessage()
mensagem['From'] = remetente
mensagem['To'] = ', '.join(destinatarios)
mensagem['Subject'] = assunto
mensagem.set_content(body)
safe = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=safe) as smtp:
    smtp.login(remetente, senha)
    smtp.sendmail(remetente, destinatarios, mensagem.as_string())
