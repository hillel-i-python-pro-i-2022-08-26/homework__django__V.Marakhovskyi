from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from apps.users.models import User

# class UserCustomAdmin(admin.ModelAdmin):
#     list_display = ('avatar', 'username', 'first_name', 'last_name', 'email')


admin.site.register(User, UserAdmin)
