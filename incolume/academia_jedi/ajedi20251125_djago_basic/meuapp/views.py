from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from datetime import datetime
from pytz import timezone


# Create your views here.
def home(request: HttpRequest) -> HttpResponse:
    """Home."""
    hora_atual = datetime.now(tz=timezone('America/Sao_Paulo'))

    return HttpResponse(f'São {hora_atual}')

def saudacao(request: HttpRequest, nome: str= '') -> HttpResponse:
    """Saudação."""
    nome = nome.capitalize() or 'Visitante'
    msg = f'Olá {nome}, Seja bem vind{"a" if nome.endswith("a") else "o"}!'

    return HttpResponse(msg)

