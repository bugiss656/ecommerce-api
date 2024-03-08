from django.urls import path
from .views import (
    ProductListView, 
    CategoriesView, 
    SubcategoriesView, 
    ProductsByCategoryView,
    ProductDetailView
)


app_name = 'products'

urlpatterns = [
    path('product/<str:slug>', ProductDetailView.as_view(), name='product'),
    path('<str:category>', ProductsByCategoryView.as_view(), name='products_by_category'),
    path('subcategories/<str:category>', SubcategoriesView.as_view(), name='subcategories'),
    path('categories/', CategoriesView.as_view(), name='categories'),
    path('all/', ProductListView.as_view(), name='products'),
]