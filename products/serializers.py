from rest_framework import serializers
from .models import (
    Category,
    Supplier,
    Product,
    Image
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


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = [
            'alt',
            'image_number',
            'image',
            'product'
        ]


class ProductSerializer(serializers.ModelSerializer):
    images = ImageSerializer(
        many=True,
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
            'main_image',
            'description',
            'images'
        ]