from rest_framework import serializers
from .models import (
    Order,
    OrderItem,
    ShippingAddress
)



class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = [
            'order',
            'product',
            'quantity'
        ]


class ShippingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingAddress
        fields = [
            'order',
            'street',
            'building_number',
            'city',
            'zip_code'
        ]


class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Order
        fields = [
            'user',
            'status',
            'created',
            'updated',
            'order_items'
        ]