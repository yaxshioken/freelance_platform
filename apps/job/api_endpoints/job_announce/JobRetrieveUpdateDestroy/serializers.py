from rest_framework import serializers

from apps.job.models import JobAnnounce


class JobRetrieveUpdateDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model=JobAnnounce
        fields='__all__'
        read_only_fields=('id',)