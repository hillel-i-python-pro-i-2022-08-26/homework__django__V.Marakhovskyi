from django.views.generic import UpdateView

from apps.contacts.models import Contact


# def update_contact(request: HttpRequest, pk: int) -> HttpResponse:
#     contact = Contact.objects.get(pk=pk)
#     if request.method == "POST":
#         form = ContactForm(request.POST, instance=contact)
#         if form.is_valid():
#             form.save()
#             return redirect("contacts:read")
#         return render(request, "contacts/contact_create_form.html", {"form": form})
#     else:
#         form = ContactForm(instance=contact)
#     return render(request, "contacts/contact_create_form.html", {"form": form})


class ContactUpdateView(UpdateView):
    model = Contact
    fields = (
        "full_name",
        "date_of_birth",
        "phone_number",
        "photo",
    )
    template_name_suffix = "_update_form"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Edit"
        return context
