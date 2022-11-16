import uuid

from django.db import models
from django.urls import reverse

from apps.contacts.typing import T_NAME


class Group(models.Model):
    relationship = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.relationship

    __repr__ = __str__


def get_photo_path(instance, filename: str) -> str:
    _, extension = filename.rsplit(".", maxsplit=1)
    return f"contacts/contact/photo/{instance.pk}/{uuid.uuid4()}/avatar.{extension}"


class Contact(models.Model):
    full_name: T_NAME = models.CharField(max_length=120)
    phone_number = models.CharField(max_length=30)
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    is_auto_generated = models.BooleanField(default=False)

    group = models.ForeignKey(
        Group, related_name="contacts", on_delete=models.CASCADE, default=None, blank=True, null=True
    )
    photo = models.ImageField(max_length=255, blank=True, null=True, upload_to=get_photo_path)

    def get_absolute_url(self):
        return reverse("contacts:update", kwargs={"pk": self.pk})

    def __str__(self) -> str:
        return f"{self.full_name} - {self.phone_number}"

    __repr__ = __str__
