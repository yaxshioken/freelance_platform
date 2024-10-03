from rest_framework import permissions
from rest_framework_simplejwt.views import (TokenObtainSlidingView,
                                            TokenViewBase)

from apps.account.api_endpoints.auth.Login.serializers import LoginSerializer


class LoginView(TokenViewBase):
    serializer_class = LoginSerializer
    permission_classes = (permissions.AllowAny,)


__all__ = ("LoginView",)
