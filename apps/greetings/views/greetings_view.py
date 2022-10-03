from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from apps.greetings.services.generate_random_name import generate_name


def greetings_view(request: HttpRequest, name: str | None = None) -> HttpResponse:
    if name is None:
        name = generate_name()
    return render(
        request,
        "greetings/index.html",
        {
            "greetings": f"Hello {name}, nice to meet you!",
        },
    )
