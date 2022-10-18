from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect

from apps.contacts.models import Contact


def contact_delete(request: HttpRequest, pk: int) -> HttpResponse:
    contact = Contact.objects.get(pk=pk)
    contact.delete()
    return redirect("contacts:read")
