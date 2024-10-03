from rest_framework import serializers

from apps.account.models import Notifications


class NotificationListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Notifications
        fields='__all__'
        read_only_fields=('id','account')
