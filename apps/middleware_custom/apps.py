from django.apps import AppConfig


class MiddlewareCustomConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.middleware_custom"
