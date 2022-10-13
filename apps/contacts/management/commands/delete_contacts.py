import logging

from django.core.management import BaseCommand
from django.utils import timezone

from apps.contacts import models


class Command(BaseCommand):
    help = "Delete contacts"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.logger = logging.getLogger("django")

    def handle(self, *args, **options):
        current_amount = models.Contact.objects.all().count()
        self.logger.info(f"Current amount of contacts: {current_amount}")

        query = models.Contact.objects

        required_datetime = timezone.now() - timezone.timedelta(seconds=10)
        query = query.order_by("created_at").filter(created_at__lt=required_datetime).filter(is_auto_generated=True)
        total_amount, details = query.delete()

        self.logger.info(f"Amount of deleted contacts : {total_amount}")

        amount_after_generating = models.Contact.objects.all().count()
        self.logger.info(f"Amount of contacts after action: {amount_after_generating}")
