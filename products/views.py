from rest_framework import (
    generics,
    viewsets,
    permissions
)
from products.models import Category, Product
from products.serializers import ProductSerializer, CategorySerializer


class CategoriesView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class SubcategoriesView(generics.ListAPIView):
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        category = self.kwargs['category']
        return Category.objects.filter(parent_category__slug=category)


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ProductsByCategoryView(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def _split_params(self, queryset):
        return queryset.split(',')

    def get_queryset(self):
        category = self.kwargs['category']
        supplier = self.request.query_params.get('supplier')
        price_min = self.request.query_params.get('price_min')
        price_max = self.request.query_params.get('price_max')
        colour = self.request.query_params.get('colour')

        queryset = Product.objects.filter(category__slug=category)

        if supplier:
            supplier_ids = self._split_params(supplier)
            queryset = queryset.filter(supplier__id__in=supplier_ids)
        if price_min:
            price_min_to_int = int(price_min)
            queryset = queryset.filter(price__gte=price_min_to_int)
        if price_max:
            price_max_to_int = int(price_max)
            queryset = queryset.filter(price__lte=price_max_to_int)
        if colour:
            colour_ids = self._split_params(colour)
            queryset = queryset.filter(attributes__id__in=colour_ids)
        
        return queryset
    

class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = 'slug'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)