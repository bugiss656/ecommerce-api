import uuid
from decimal import Decimal
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from tinymce import models as tinymce_models


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

    slug = models.SlugField(
        default='',
        null=True,
        blank=True
    )

    image = models.ImageField(
        verbose_name='Zdjęcie kategorii',
        default=''
    )

    parent_category = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        related_name='subcategories',
        on_delete=models.CASCADE
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

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


class ProductAttribute(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    name = models.CharField(
        verbose_name='Nazwa atrybutu produktu',
        max_length=200,
        default=''
    )

    display_name = models.CharField(
        verbose_name='Nazwa atrybutu do wyświetlenia (PL)',
        max_length=200,
        default=''
    )

    category = models.ManyToManyField(
        Category,
        default=''
    )

    def __str__(self):
        return self.display_name


class ProductAttributeValue(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    product_attribute = models.ForeignKey(
        ProductAttribute,
        related_name='attributes',
        on_delete=models.CASCADE,
    )

    value = models.CharField(
        verbose_name='Opis parametru',
        max_length=200,
        default=''
    )

    def __str__(self):
        return f'{self.product_attribute.display_name} - {self.value}'


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

    slug = models.SlugField(
        default='',
        null=True,
        blank=True
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
        max_digits=7,
        decimal_places=2,
        default=Decimal(00.00)
    )

    attributes = models.ManyToManyField(
        ProductAttributeValue,
        default=''
    )

    main_image = models.ImageField(
        verbose_name='Zdjęcie główne',
        default=''
    )

    description = tinymce_models.HTMLField(
        verbose_name='Opis produktu',
        blank=True,
        null=True,
        max_length=10000,
        default=''
    )

    created = models.DateTimeField(
        default=timezone.now
    )

    updated = models.DateTimeField(
        auto_now=True
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


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