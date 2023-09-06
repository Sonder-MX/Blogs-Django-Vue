from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .serializers import RefreshTokenSerializer, TokenSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    """自定义 token 视图"""

    serializer_class = TokenSerializer


class CustomTokenRefreshView(TokenRefreshView):
    """自定义 refresh 视图"""

    serializer_class = RefreshTokenSerializer
