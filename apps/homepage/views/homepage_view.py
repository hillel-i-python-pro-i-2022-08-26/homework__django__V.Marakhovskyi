from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from apps.homepage.services.generate_welcome_message import generate_welcome_message


def homepage_view(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        "index.html",
        {
            "welcome_message": generate_welcome_message(),
            "title": "Welcome",
        },
    )
