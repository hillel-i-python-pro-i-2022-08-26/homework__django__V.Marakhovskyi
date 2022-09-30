from django.http import HttpRequest, HttpResponse

from apps.greetings.services.default_greetings import default_greetings


def default_greet_view(request: HttpRequest) -> HttpResponse:
    return HttpResponse(default_greetings())
