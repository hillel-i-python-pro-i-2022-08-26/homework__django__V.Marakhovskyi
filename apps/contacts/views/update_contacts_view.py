from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from apps.contacts.forms import ContactForm
from apps.contacts.models import Contact


def update_contact(request: HttpRequest, id: int) -> HttpResponse:
    contact = Contact.objects.get(pk=id)
    if request.method == "POST":
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect("contacts:read")
        return render(request, "contacts/form.html", {"form": form})
    else:
        form = ContactForm(instance=contact)
    return render(request, "contacts/form.html", {"form": form})
