from rest_framework import generics, permissions
from .models import Banner
from .serializers import BannerSerializer


class BannerListView(generics.ListAPIView):
    queryset = Banner.objects.all().filter(is_active=True)
    serializer_class = BannerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]