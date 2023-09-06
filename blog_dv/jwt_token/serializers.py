from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer,
    TokenRefreshSerializer,
)
from rest_framework_simplejwt.state import token_backend


class TokenSerializer(TokenObtainPairSerializer):
    """自定义获取token序列化器"""

    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)  # 获取Token对象
        # data["refresh"] = str(refresh)  # 不添加也会默认返回
        # data["access"] = str(refresh.access_token)
        data["username"] = self.user.username
        data["token_exp"] = refresh.access_token.payload["exp"]  # access_token过期时间
        return data

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        return token


class RefreshTokenSerializer(TokenRefreshSerializer):
    """自定义刷新token序列化器"""

    def validate(self, attrs):
        data = super(RefreshTokenSerializer, self).validate(attrs)
        decoded_payload = token_backend.decode(data["access"], verify=True)
        data["token_exp"] = decoded_payload["exp"]  # access_token过期时间
        return data
