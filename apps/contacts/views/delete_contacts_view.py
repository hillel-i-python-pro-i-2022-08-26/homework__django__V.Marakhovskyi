from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect

from apps.contacts.models import Contact


def contact_delete(request: HttpRequest, id: int) -> HttpResponse:
    contact = Contact.objects.get(pk=id)
    contact.delete()
    return redirect("contacts:index")
