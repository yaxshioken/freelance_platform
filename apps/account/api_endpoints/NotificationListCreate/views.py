from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView

from apps.account.api_endpoints.NotificationListCreate.serializers import NotificationListCreateSerializer
from apps.account.models import Notifications


class NotificationView(ListCreateAPIView):
    serializer_class = NotificationListCreateSerializer
    queryset = Notifications.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
           type = self.request.query_params.get("type", None)
           is_read = self.request.query_params.get("is_read", None)
           if type:
               queryset = self.queryset.filter(type=type)
           if is_read:
               queryset = self.queryset.filter(is_read=is_read)
           return queryset().filter(is_read=self.request.user.accountinfo_set)
__all__="NotificationViewSet"
