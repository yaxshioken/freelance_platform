from rest_framework.serializers import ModelSerializer

from apps.job.models import JobTechnology


class JobTechnologyListCreateSerializer(ModelSerializer):
    class Meta:
        model = JobTechnology
        fields = ("id", "job", "technology", "level")
