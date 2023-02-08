from rest_framework import generics

from apps.contacts.models import Contact
from apps.crud_drf.serializers import ContactSerializer


class ContactAPIView(generics.ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
