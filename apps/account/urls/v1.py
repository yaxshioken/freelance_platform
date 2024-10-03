
from django.urls import path

from apps.account.api_endpoints.NotificationRetrieveUpdate import NotificationRetrieveView
from apps.account.api_endpoints.activation import (SendActivationCodeView,
                                                   VerificationCodeView)
from apps.account.api_endpoints.auth.Login.views import LoginView
from apps.account.api_endpoints.auth.Register.views import \
    RegisterListCreateView
from apps.account.api_endpoints.NotificationListCreate.views import NotificationView

urlpatterns = [
    path("register/", RegisterListCreateView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("send-code/", SendActivationCodeView.as_view(),name="send-activation-code"),
    path("verify-code/", VerificationCodeView.as_view(),name="verify-code"),
    path("notifications/", NotificationView.as_view(), name="notifications"),
    path("notification/<pk>", NotificationRetrieveView.as_view(), name="notification-detail")
    ,
]


