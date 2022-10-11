from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from apps.userdata.services import generate_userlist


# Create your views here.


def get_userlist(request: HttpRequest, amount=None) -> HttpResponse:
    if amount is None:
        amount = 10
    return render(
        request,
        "userdata/index.html",
        {
            "userdata": generate_userlist(amount=amount),
            "title": "Userdata",
        },
    )
