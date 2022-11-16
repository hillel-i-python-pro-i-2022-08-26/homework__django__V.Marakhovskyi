from django import forms

from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ("full_name", "phone_number", "date_of_birth", "photo")
