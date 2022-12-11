import uuid
from decimal import Decimal
from django.db import models


class Category(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    name = models.CharField(
        verbose_name='Nazwa kategorii',
        default='',
        max_length=200
    )

    is_active = models.BooleanField(
        verbose_name='Aktywna?',
        default=True
    )


class Supplier(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    name = models.CharField(
        verbose_name='Nazwa firmy',
        default='',
        max_length=200
    )


class Product(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    name = models.CharField(
        verbose_name='Nazwa produktu',
        default='',
        max_length=200
    )

    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.CASCADE
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )

    is_active = models.BooleanField(
        verbose_name='Aktywny',
        default=True
    )

    stock_quantity = models.IntegerField(
        verbose_name='Ilość w magazynie',
        default=0
    )

    price = models.DecimalField(
        verbose_name='Cena',
        max_digits=15,
        decimal_places=2,
        default=Decimal(00.00)
    )

    image = models.ImageField(
        verbose_name='Zdjęcie główne',
        default=''
    )

    description = models.TextField(
        verbose_name='Opis produktu',
        default='',
        max_length=1000
    )