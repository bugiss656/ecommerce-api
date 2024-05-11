from rest_framework import (
    views,
    generics,
    authentication,
    permissions,
    status
)
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from .serializers import (
    UserSerializer,
    AuthTokenSerializer
)
from rest_framework.permissions import AllowAny
from django.shortcuts import get_object_or_404
from .models import User


class RegisterUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class CreateTokenView(ObtainAuthToken):
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ManageUserView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
    

class CheckPasswordView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id, *args, **kwargs):
        user = get_object_or_404(User, id=user_id)

        provided_password = request.data.get('password')

        if user.check_password(provided_password):
            return Response({'message': 'Password is correct'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Password is incorrect'}, status=status.HTTP_400_BAD_REQUEST)


class UpdateProfileView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]