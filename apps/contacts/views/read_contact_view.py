from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from apps.contacts.models import Contact


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
