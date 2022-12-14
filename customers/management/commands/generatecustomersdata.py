from faker import Faker
from django.db import transaction
from django.core.management.base import BaseCommand, CommandError

from django.contrib.auth.models import User
from customers.models import (
    CustomerProfile,
    Address
)


DATA_COUNT = 10
fake = Faker()


class Command(BaseCommand):
    help = 'Generates customers testing data.'

    @transaction.atomic
    def handle(self, *args, **kwargs):

        from django.conf import settings
        if not settings.DEBUG:
            raise CommandError('Generating test data available only for DEBUG=True')

        self.stdout.write('Cleaning database...')
          
        User.objects.filter(is_superuser=False).delete()
        CustomerProfile.objects.all().delete()
        Address.objects.all().delete()
        
        for _ in range(DATA_COUNT):
            User.objects.create(
                username = fake.user_name(),
                first_name = fake.first_name(),
                last_name = fake.last_name(),
                email = fake.email()
            )

        users = User.objects.filter(is_superuser=False)

        for i in range(DATA_COUNT):
            CustomerProfile.objects.create(
                user = users[i],
                phone = fake.phone_number()
            )

        for i in range(DATA_COUNT):
            Address.objects.create(
                user = users[i],
                street = fake.street_name(),
                building_number = fake.building_number(),
                city = fake.city(),
                zip_code = fake.postcode()
            )

        self.stdout.write('Testing data created...')
        
        