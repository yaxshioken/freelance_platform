from django.urls import path

from apps.account.api_endpoints.activation import (SendActivationCodeView,
                                                   VerificationCodeView)
from apps.account.api_endpoints.auth.Login.views import LoginView
from apps.account.api_endpoints.auth.Register.views import \
    RegisterListCreateView

urlpatterns = [
    path("register/", RegisterListCreateView.as_view(), name="Register"),
    path("login/", LoginView.as_view(), name="Login"),
    path("send-code/", SendActivationCodeView.as_view()),
    path("verify-code/", VerificationCodeView.as_view()),
]
