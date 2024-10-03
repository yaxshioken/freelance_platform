from rest_framework.serializers import ModelSerializer

from apps.job.models import JobLocation


class JobLocationListCreateSerializer(ModelSerializer):
    class Meta:
        model = JobLocation
        fields = ("id", "city", "country")
