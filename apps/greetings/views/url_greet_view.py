from django.http import HttpRequest, HttpResponse
from apps.greetings.services.url_greetings import url_greetings

def url_greet_view(request:HttpRequest, name:str) -> HttpResponse:
    return HttpResponse(url_greetings(name=name))