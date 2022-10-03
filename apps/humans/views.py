from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from apps.humans.services import generate_humans


# Create your views here.


def get_humans(request: HttpRequest, amount=None) -> HttpResponse:
    if amount is None:
        amount = 10
    return render(
        request,
        "humans/index.html",
        {
            "humans": generate_humans(amount=amount),
            "title": "Humans",
        },
    )
