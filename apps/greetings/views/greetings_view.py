from django.http import HttpRequest, HttpResponse

from apps.greetings.services.generate_random_name import generate_name


# render


def greetings_view(request: HttpRequest, name: str | None = None) -> HttpResponse:
    if name is None:
        name = generate_name()
    return HttpResponse(f"Hello, {name}, nice to meet you!")
