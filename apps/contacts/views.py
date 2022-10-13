from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .models import Contact


def get_contacts(request: HttpRequest) -> HttpResponse:
    contacts = Contact.objects.all()

    return render(
        request,
        "contacts/index.html",
        {
            "contacts": contacts,
            "title": "Contact list",
        },
    )
