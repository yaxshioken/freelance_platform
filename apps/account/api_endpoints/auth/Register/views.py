from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import AllowAny

from apps.account.api_endpoints.auth.Register.serializers import \
    RegisterSerializer
from apps.account.models import Account


class RegisterListCreateView(ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]
