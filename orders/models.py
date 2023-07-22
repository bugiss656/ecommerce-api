import uuid
from django.conf import settings
from django.db import models
from django.utils import timezone
from products.models import Product


class Order(models.Model):
    ORDER_STATUSES = (
        ('confirmed', 'Confirmed'),
        ('pending_payment', 'Pending payment'),
        ('sent', 'Order sent'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
    )

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    status = models.CharField(
        verbose_name='Status zamówienia',
        choices=ORDER_STATUSES,
        default='',
        max_length=100
    )

    created = models.DateTimeField(
        auto_now_add=True
    )

    updated = models.DateTimeField(
        auto_now=True
    )


class OrderItem(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    order = models.ForeignKey(
        Order,
        on_delete=models.SET_NULL,
        null=True
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        null=True
    )

    quantity = models.PositiveIntegerField(
        verbose_name='Zamówiona ilość',
        default=0
    )


class ShippingAddress(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    
    order = models.ForeignKey(
        Order,
        on_delete=models.SET_NULL,
        null=True
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
        return self.id