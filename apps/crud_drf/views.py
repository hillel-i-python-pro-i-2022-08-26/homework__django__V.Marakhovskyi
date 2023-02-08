from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from apps.contacts.models import Contact
from apps.crud_drf.serializers import ContactSerializer


# Allows to see all contacts
class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = (IsAuthenticated,)


class ContactAPICreate(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = (IsAuthenticated,)


# Allows to see one exact contact
class ContactAPIRead(generics.RetrieveAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = (IsAuthenticated,)


class ContactAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = (IsAuthenticated,)


class ContactAPIDelete(generics.RetrieveDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = (IsAuthenticated,)
