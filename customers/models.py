from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class AutoDateTimeField(models.DateTimeField):
    def pre_save(self, model_instance, add):
        return timezone.now()


class Address(models.Model):
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
    

class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    address = models.OneToOneField(
        Address,
        on_delete=models.CASCADE
    )

    phone = models.CharField(
        verbose_name='Telefon',
        blank=True,
        null=True,
        default='',
        max_length=200
    )

    created = AutoDateTimeField(
        default=timezone.now()
    )