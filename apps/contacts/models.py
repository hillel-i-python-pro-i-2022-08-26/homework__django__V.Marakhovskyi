from django.db import models

from apps.contacts.typing import T_NAME


class Contact(models.Model):
    full_name: T_NAME = models.CharField(max_length=120)
    phone_number = models.CharField(max_length=30)
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    is_auto_generated = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.full_name} - {self.phone_number}"

    __repr__ = __str__
