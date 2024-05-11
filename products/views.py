from rest_framework import (
    generics,
    viewsets,
    permissions,
    views
)
from rest_framework.response import Response
from products.models import (
    Category, 
    Supplier, 
    Product, 
    ProductAttribute, 
    ProductAttributeValue
)
from products.serializers import ProductSerializer, CategorySerializer, ProductAttributeValueSerializer


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


class SuppliersByCategoryView(views.APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, *args, **kwargs):
        try:
            category_slug = self.kwargs['category']
            category = Category.objects.get(slug=category_slug)
            suppliers = Supplier.objects.filter(product__category=category).distinct()
            suppliers_data = []
            for supplier in suppliers:
                products_count = Product.objects.filter(category=category, supplier=supplier).count()
                suppliers_data.append({
                    'id': supplier.id,
                    'name': supplier.name,
                    'products_count': products_count
                })
            return Response(suppliers_data, status=200)
        except Category.DoesNotExist:
            return Response({'message': 'Category not found'}, status=404)


class AttributesByCategoryView(views.APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        try:
            category_slug = self.kwargs['category']
            category = Category.objects.get(slug=category_slug)
            attributes = ProductAttribute.objects.filter(category=category)
            attributes_data = []
            for attribute in attributes:
                attribute_values = ProductAttributeValue.objects.filter(product_attribute=attribute).values('value')
                serializer = ProductAttributeValueSerializer(attribute_values, many=True)
                attributes_data.append({
                    'name': attribute.name,
                    'display_name': attribute.display_name,
                    'values': serializer.data
                })
            return Response(attributes_data, status=200)
        except Category.DoesNotExist:
            return Response({'message': 'Category not found'}, status=404)


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
        suppliers = self.request.query_params.getlist('supplier')
        price_min = self.request.query_params.get('priceMin')
        price_max = self.request.query_params.get('priceMax')

        queryset = Product.objects.filter(category__slug=category)

        if suppliers:
            queryset = queryset.filter(supplier__name__in=suppliers)
        if price_min:
            price_min_to_int = int(price_min)
            queryset = queryset.filter(price__gte=price_min_to_int)
        if price_max:
            price_max_to_int = int(price_max)
            queryset = queryset.filter(price__lte=price_max_to_int)

        for param in self.request.query_params:
            if param != 'supplier' and param != 'priceMin' and param != 'priceMax':
                queryset = queryset.filter(
                    attributes__product_attribute__name=param,
                    attributes__value__in=self.request.query_params.getlist(param)
                ).distinct()
                
        return queryset
    

class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = 'slug'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)