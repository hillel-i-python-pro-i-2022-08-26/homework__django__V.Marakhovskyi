from django.shortcuts import render

from apps.contacts.forms import ContactForm


def crud_contacts(request):
    form = ContactForm()
    return render(request, "contacts/form.html", {"form": form})
