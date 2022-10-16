from django.shortcuts import redirect, render

from apps.contacts.forms import ContactForm
from apps.contacts.models import Contact


def update_contact(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = ContactForm()
        else:
            contact = Contact.objects.get(pk=id)
            form = ContactForm(instance=contact)
        return render(request, "contacts/form.html", {"form": form})
    else:
        if id == 0:
            form = ContactForm(request.POST)
        else:
            contact = Contact.objects.get(pk=id)
            form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
        return redirect("contacts:index")
