from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
def geek_home(request: HttpRequest) -> HttpResponse:
    """View function for the geek home page."""
    return HttpResponse("Welcome to the Geek Home Page!")

