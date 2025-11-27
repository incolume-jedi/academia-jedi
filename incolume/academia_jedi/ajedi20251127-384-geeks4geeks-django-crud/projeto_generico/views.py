"""Views."""
from django.http import HttpResponse

def hello_geeks(request):
    return HttpResponse("Hello Geeks")

