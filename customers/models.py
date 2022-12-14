import uuid
from django.db import models
from django.contrib.auth.models import User
    


class CustomerProfile(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    phone = models.CharField(
        verbose_name='Telefon',
        blank=True,
        null=True,
        default='',
        max_length=200
    )

    modified_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f'{self.user.get_username()} - {self.user.email}'


class Address(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    street = models.CharField(
        verbose_name='Ulica zamieszkania',
        blank=True,
        null=True,
        default='',
        max_length=200
    )

    building_number = models.CharField(
        verbose_name='Numer domu/lokalu',
        blank=True,
        null=True,
        default='',
        max_length=200
    )

    city = models.CharField(
        verbose_name='Miasto',
        blank=True,
        null=True,
        default='',
        max_length=200
    )

    zip_code = models.CharField(
        verbose_name='Kod pocztowy',
        blank=True,
        null=True,
        default='',
        max_length=200
    )

    def __str__(self):
        return f'{self.street} {self.building_number} - {self.user.email}'