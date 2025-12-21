from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from . import models


# Create your views here.
def geek_home(request: HttpRequest) -> HttpResponse:
    """View function for the geek home page."""
    return HttpResponse('Welcome to the Geek Home Page!')


def list_view(request: HttpRequest) -> HttpResponse:
    """List view function to display all GeekModel entries."""
    # dictionary for initial data with field names as keys
    context = {}

    # add the dictionary during initialization
    context['dataset'] = models.GeeksModel.objects.all()
    return render(request, 'list_view.html', context)
