from rest_framework import serializers
from .models import Banner


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = [
            'title', 
            'is_active', 
            'ordering_number', 
            'image', 
            'href'
        ]
        