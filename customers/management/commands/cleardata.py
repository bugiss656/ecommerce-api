from django.db import transaction
from django.core.management.base import BaseCommand, CommandError

from django.contrib.auth.models import User
from customers.models import (
    CustomerProfile,
    Address
)   


class Command(BaseCommand):
    help = 'Generates customers testing data.'

    @transaction.atomic
    def handle(self, *args, **kwargs):

        from django.conf import settings
        if not settings.DEBUG:
            raise CommandError('Clearing data available only for DEBUG=True')
          
        User.objects.filter(is_superuser=False).delete()
        CustomerProfile.objects.all().delete()
        Address.objects.all().delete()

        self.stdout.write('Database cleaned...')