from django.db import transaction
from django.core.management.base import BaseCommand, CommandError

from customers.models import (
    User
)   


class Command(BaseCommand):
    help = 'Generates customers testing data.'

    @transaction.atomic
    def handle(self, *args, **kwargs):

        from django.conf import settings
        if not settings.DEBUG:
            raise CommandError('Clearing data available only for DEBUG=True')
          
        User.objects.filter(is_superuser=False).delete()

        self.stdout.write('Database cleaned...')