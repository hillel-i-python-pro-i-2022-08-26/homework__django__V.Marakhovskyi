# from django.http import HttpRequest, HttpResponse
# from django.shortcuts import render
#
# from apps.contacts.models import Contact
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
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


class ArticleListView(LoginRequiredMixin, ListView):
    login_url = "/auth/login"
    model = Contact

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Contacts"
        return context

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.warning(request, "Only authorized users have access to this page.")
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)
