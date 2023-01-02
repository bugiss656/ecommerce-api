from rest_framework import serializers
from .models import (
    Order,
    OrderItem,
    ShippingAddress
)
from customers.serializers import UserSerializer
from products.serializers import ProductSerializer



class OrderSerializer(serializers.ModelSerializer):
    user = UserSerializer(
        read_only=True
    )

    class Meta:
        model = Order
        fields = [
            'user',
            'status',
            'created',
            'updated'
        ]


class OrderItemSerializer(serializers.ModelSerializer):
    order = OrderSerializer(
        read_only=True
    )
    product = ProductSerializer(
        read_only=True
    )

    class Meta:
        model = OrderItem
        fields = [
            'order',
            'product',
            'quantity'
        ]


class ShippingAddressSerializer(serializers.ModelSerializer):
    order = OrderSerializer(
        read_only=True
    )

    class Meta:
        model = ShippingAddress
        fields = [
            'order',
            'street',
            'building_number',
            'city',
            'zip_code'
        ]