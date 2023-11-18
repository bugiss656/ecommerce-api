import os
from pathlib import Path
from faker import Faker
from django.conf import settings
from django.core.files import File
from django.db import transaction
from django.core.management.base import BaseCommand, CommandError

from banners.models import Banner


DATA_COUNT = 3
fake = Faker()

def get_image_names(path):
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif']
    image_names = []

    for filename in os.listdir(path):
        if any(filename.lower().endswith(extension) for extension in image_extensions):
            image_names.append(filename)
    
    return image_names

class Command(BaseCommand):
    help = 'Generates banners testing data'

    @transaction.atomic
    def handle(self, *args, **kwargs):

        base_path = settings.BASE_DIR / 'mockdata/banners'
        images = get_image_names(base_path)

        if not settings.DEBUG:
            raise CommandError('Generating test data available only for DEBUG=True')

        for image in images:
            image_path =  base_path / image

            if os.path.exists(image_path):
                with image_path.open(mode='rb') as image_file:
                    try:
                        Banner.objects.create(
                            title=fake.bs(),
                            is_active=fake.boolean(),
                            ordering_number=0,
                            image=File(image_file, name=image),
                            href=None
                        )

                        self.stdout.write(self.style.SUCCESS('Banners data created'))
                    except Exception as e:
                        self.stdout.write(self.style.ERROR(f'Error creating Banner: {e}'))
            else:
                self.stdout.write(self.style.ERROR(f'Image not found at path: {image_path}'))