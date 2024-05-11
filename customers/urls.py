from django.urls import path
from .views import (
    RegisterUserView,
    CreateTokenView,
    ManageUserView,
    CheckPasswordView,
    UpdateProfileView
)


app_name = 'customers'

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('token/', CreateTokenView.as_view(), name='token'),
    path('user/', ManageUserView.as_view(), name='user'),
    path('update/<int:pk>', UpdateProfileView.as_view(), name='update'),
    path('check-password/<int:user_id>', CheckPasswordView.as_view(), name='check_password')
]