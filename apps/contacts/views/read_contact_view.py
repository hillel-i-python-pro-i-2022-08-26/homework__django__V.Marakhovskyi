# from django.http import HttpRequest, HttpResponse
# from django.shortcuts import render
#
# from apps.contacts.models import Contact
from django.views.generic import ListView

from apps.contacts.models import Contact


# def get_contacts(request: HttpRequest) -> HttpResponse:
#     contacts = Contact.objects.all()
#
#     return render(
#         request,
#         "contacts/contact_list.html",
#         {
#             "contacts": contacts,
#             "title": "Contact list",
#         },
#     )
class ArticleListView(ListView):

    model = Contact

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Contacts"
        return context
