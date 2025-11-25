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

def produtos(request: HttpRequest, id_produto: int) -> HttpResponse:
    """Produtos."""
    produtos ={
        1: 'produto1',
        2: 'produto2',
        3: 'produto3',
        4: 'produto4',
        5: 'produto5',
        6: 'produto6',
        7: 'produto7',
    }
    produto = produtos.get(id_produto, 'Produto não encontrado.')
    return HttpResponse(f'{produto}')
