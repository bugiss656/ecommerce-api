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

    parent_category = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        related_name='children',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


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

    def __str__(self):
        return self.name


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

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )

    supplier = models.ForeignKey(
        Supplier,
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
        max_digits=5,
        decimal_places=2,
        default=Decimal(00.00)
    )

    main_image = models.ImageField(
        verbose_name='Zdjęcie główne',
        default=''
    )

    description = models.TextField(
        verbose_name='Opis produktu',
        default='',
        max_length=1000
    )


class Image(models.Model):
    alt = models.CharField(
        'Tekst alternatywny (nazwa zdjęcia)', 
        max_length=60, 
        null=True, 
        blank=True, 
        default=''
    )

    image_number = models.IntegerField(
        'Numer zdjęcia',
        null=True
    )

    image = models.ImageField(
        null=True, 
        blank=True, 
        upload_to='images', 
        default=''
    )

    product = models.ForeignKey(
        Product,
        related_name='images',
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ['image_number']

    def __str__(self):
        return self.alt