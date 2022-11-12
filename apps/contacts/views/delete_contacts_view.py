from django.urls import reverse_lazy
from django.views.generic import DeleteView

from apps.contacts.models import Contact


# def contact_delete(request: HttpRequest, pk: int) -> HttpResponse:
#     contact = Contact.objects.get(pk=pk)
#     contact.delete()
#     return redirect("contacts:read")


class ContactDeleteView(DeleteView):
    model = Contact
    success_url = reverse_lazy("contacts:read")
