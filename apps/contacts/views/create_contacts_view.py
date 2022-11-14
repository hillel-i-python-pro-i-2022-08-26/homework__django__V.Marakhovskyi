from django.urls import reverse_lazy
from django.views.generic import CreateView

from apps.contacts.models import Contact


# def crud_contacts(request: HttpRequest) -> HttpResponse:
#     if request.method == "POST":
#         form = ContactForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect("contacts:read")
#     else:
#         form = ContactForm()
#     return render(request, "contacts/contact_create_form.html", {"form": form})


class ContactCreateView(CreateView):
    model = Contact
    fields = ["full_name", "phone_number", "date_of_birth", "photo"]
    template_name_suffix = "_create_form"
    # By default, the class looks for 'the get_absolute_url' function.
    # Here purposefully it is redefined for practical purposes.
    success_url = reverse_lazy("contacts:read")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Create"
        return context
