from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
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

    street = models.CharField(
        verbose_name='Ulica zamieszkania',
        blank=True,
        null=True,
        default='',
        max_length=200
    )

    street_number = models.CharField(
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

    created = models.DateField(
        auto_now_add=True
    )
