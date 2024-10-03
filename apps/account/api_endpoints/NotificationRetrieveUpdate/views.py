
from rest_framework.generics import  RetrieveAPIView

from apps.account.api_endpoints.NotificationRetrieveUpdate.serializers import NotificationRetrieveSerializer
from apps.account.models import Notifications


class NotificationRetrieveView(RetrieveAPIView):
    queryset = Notifications.objects.all()
    serializer_class = NotificationRetrieveSerializer
    def get_object(self):
        notification=super().get_object()
        notification.mark_as_read()
        return notification
__all__ = ['NotificationRetrieveView']
