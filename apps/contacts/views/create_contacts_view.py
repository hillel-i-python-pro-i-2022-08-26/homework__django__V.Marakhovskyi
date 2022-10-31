from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

from apps.contacts.forms import ContactForm


def crud_contacts(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("contacts:read")
    else:
        form = ContactForm()
    return render(request, "contacts/form.html", {"form": form})