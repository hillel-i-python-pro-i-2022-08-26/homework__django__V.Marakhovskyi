from django.http import HttpRequest, HttpResponse

from apps.greetings.services.default_greetings import default_greetings
from apps.greetings.services.url_greetings import url_greetings

def default_greet_view(request: HttpRequest) -> HttpResponse:
    return HttpResponse(default_greetings())

def url_greet_view(request:HttpRequest, name:str) -> HttpResponse:
    return HttpResponse(url_greetings(name=name))


