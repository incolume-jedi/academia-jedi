"""Email with python."""

import json
import mimetypes
import os
import smtplib
import ssl
from email.message import EmailMessage
from pathlib import Path

from icecream import ic
from incolume.academia_jedi import logger

__all__ = ['EmailMessage', 'smtplib', 'ssl', 'os', 'mimetypes', 'Path']

def send_email(credentials_file: Path |None = None, **kwargs) -> bool:
    """Send email with python.
    Args:
        credentials_file (Path | None): Path to the credentials file.
        **kwargs: Optional arguments.
            assunto (str): Subject of the email.
            template_conteudo (Path): Path to the email content template.
            destinatarios (list[str]): List of email recipients.
            sing (str): Signature of the email.
    Returns:
        bool: True if the email was sent successfully, False otherwise.
    Raises:

    """


    logger.info(ic('Iniciando o envio de email...'))

    assunto: str = kwargs.get('assunto', 'Relatório mensal')
    logger.info(ic(f'Assunto: {assunto}'))

    template_conteudo: Path = kwargs.get('template_conteudo', Path(__file__).parent.joinpath('content_txt.txt'))
    logger.info(ic(f'Template de conteúdo: {template_conteudo}'))

    destinatarios: list[str] = kwargs.get('destinatarios',[
        'jesoxid995@benznoi.com',  # email gerado por temp-mail.org
    ])
    logger.info(ic(f'Destinatários: {destinatarios}'))

    credentials_file = credentials_file or Path(__file__).parents[3].joinpath('credentials', 'credentials.json')

    sing: str = kwargs.get('sing', """

        Ricardo Brito do Nascimento
        Analista de Sistemas
        Junta Especializada de Desenvolvimento e Inovação
        Desenvolvimento Incolume""")

    with credentials_file.open() as f:
        data = json.load(f)
        remetente = data['email']
        senha = data['google_password']

    logger.info(ic(f'Remetente: {remetente}'))

    body = template_conteudo.read_text()
    body = body.format(
        sign=sing,
    )
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
    logger.info(ic('Email enviado com sucesso!'))
    return True


if __name__ == '__main__':
    send_email()
