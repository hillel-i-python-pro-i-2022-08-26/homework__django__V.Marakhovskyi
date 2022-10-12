from django.db import models

from apps.animals.typing import T_NAME


class Animal(models.Model):
    name: T_NAME = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField()

    is_auto_generated = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.name} - {self.age}"

    __repr__ = __str__
