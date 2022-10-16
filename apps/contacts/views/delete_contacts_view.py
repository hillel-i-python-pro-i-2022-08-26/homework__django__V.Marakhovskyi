from django.shortcuts import redirect

from apps.contacts.models import Contact


def contact_delete(request, id):
    contact = Contact.objects.get(pk=id)
    contact.delete()
    return redirect("contacts:index")
