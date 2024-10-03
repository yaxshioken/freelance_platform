from rest_framework import serializers

from apps.job.models import JobLocation


class JobLocationRetrieveDestroyUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobLocation
        fields = '__all__'