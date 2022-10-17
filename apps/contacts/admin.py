from django.contrib import admin

from . import models

admin.site.register(models.Contact)


class ContactInline(admin.TabularInline):
    model = models.Contact


@admin.register(models.Group)
class GroupAdmin(admin.ModelAdmin):
    inlines = (ContactInline,)


# Register your models here.
