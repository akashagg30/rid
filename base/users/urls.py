# base/users/urls.py

from django.urls import path
from base.users.views import UserRegistrationView, UserLoginView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('user/register/', UserRegistrationView.as_view(), name='register'),
    path('user/login/', TokenObtainPairView.as_view(), name='login'),
    path('user/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
