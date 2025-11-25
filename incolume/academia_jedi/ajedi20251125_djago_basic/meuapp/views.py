from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from datetime import datetime
from pytz import timezone


# Create your views here.
def home(request: HttpRequest):
    """Home."""
    hora_atual = datetime.now(tz=timezone('America/Sao_Paulo'))

    return HttpResponse(f'São {hora_atual}')
