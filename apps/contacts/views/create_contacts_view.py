from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from apps.contacts.forms import ContactForm
from apps.contacts.models import Contact


def crud_contacts(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("contacts:read")
    else:
        form = ContactForm()
    return render(request, "contacts/contact_create_form.html", {"form": form})


# class ContactListView(ListView):
#     model = Contact
# class ContactCreateView(CreateView):
#     model = Contact
#     fields = ("full_name", "phone_number", "date_of_birth", "photo",)
#
#     def get_success_url(self):
#         return reverse('contacts:create', kwargs={'pk': self.object.pk})
#
#
#
# class ContactView(TemplateView):
#     template_name = "contacts/contact_create_form.html"
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         contact = Contact.objects.get(pk=context["pk"])
#         context['contact'] = contact
#         context['title'] = f"Info {contact.name}."
#         return context


class ContactCreateView(CreateView):
    model = Contact
    fields = ["full_name", "phone_number", "date_of_birth", "photo"]
    template_name_suffix = "_create_form"
    # By default, the class looks for 'the get_absolute_url' function. Here purposefully it is redefined for practical purposes.
    success_url = reverse_lazy("contacts:read")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Create"
        return context
