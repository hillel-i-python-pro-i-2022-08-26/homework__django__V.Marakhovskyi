from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.


def get_humans(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        "humans/index.html",
        {"humans": ["a"] * 10},
    )
