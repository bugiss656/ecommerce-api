from rest_framework import serializers
from .models import (
    Category,
    Supplier,
    Product
)



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'name',
            'is_active'
        ]


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = [
            'name'
        ]


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(
        read_only=True
    )
    supplier = SupplierSerializer(
        read_only=True
    )
    
    class Meta:
        model = Product
        fields = [
            'name',
            'category',
            'supplier',
            'is_active',
            'stock_quantity',
            'price',
            'image',
            'description'
        ]