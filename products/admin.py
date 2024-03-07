from django.contrib import admin
from .models import (
    Category, 
    Supplier, 
    ProductAttribute, 
    ProductAttributeValue, 
    Product, 
    Image
)


admin.site.register(Category)
admin.site.register(Supplier)
admin.site.register(ProductAttribute)
admin.site.register(ProductAttributeValue)
admin.site.register(Product)
admin.site.register(Image)