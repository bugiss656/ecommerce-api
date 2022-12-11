import uuid
from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class Order(models.Model):
    ORDER_STATUSES = (
        ('placed', 'Placed'),
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
        User,
        on_delete=models.CASCADE
    )

    status = models.CharField(
        verbose_name='Status zamówienia',
        choices=ORDER_STATUSES,
        default='',
        max_length=100
    )


class OrderItem(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    
    product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL
    )

    order = models.ForeignKey(
        Order,
        on_delete=models.SET_NULL
    )

    quantity = models.PositiveIntegerField(
        verbose_name='Zamówiona ilość',
        default=0
    )