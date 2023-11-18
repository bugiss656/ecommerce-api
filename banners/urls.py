from django.urls import path
from .views import BannerListView


appname = 'banners'

urlpatterns = [
    path('', BannerListView.as_view(), name='banners')
]