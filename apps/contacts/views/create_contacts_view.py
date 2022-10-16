from django.shortcuts import render, redirect
from django.utils import timezone

from apps.contacts.forms import ContactForm


def crud_contacts(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect("contacts:index")
    else:
        form = ContactForm()
    return render(request, "contacts/form.html", {"form": form})
