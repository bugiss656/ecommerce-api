from rest_framework import (
    generics,
    permissions
)
from products.models import Product
from products.serializers import ProductSerializer



class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
