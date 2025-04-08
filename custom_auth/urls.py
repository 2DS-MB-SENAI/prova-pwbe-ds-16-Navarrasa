from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import registro_usuarios, user_profile

urlpatterns = [
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/register/', registro_usuarios, name='register'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # protegidos por JWT
    path('auth/profile/', user_profile, name='user_profile'),
]
