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
            'id',
            'name',
            'slug',
            'image',
            'parent_category',
            'subcategories'
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['subcategories'] = CategorySerializer(instance.subcategories.all(), many=True).data
        return representation


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = [
            'id',
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
    supplier = SupplierSerializer()

    images = ImageSerializer(
        many=True,
        read_only=True
    )
    
    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'slug',
            'category',
            'supplier',
            'is_active',
            'stock_quantity',
            'price',
            'main_image',
            'description',
            'images'
        ]