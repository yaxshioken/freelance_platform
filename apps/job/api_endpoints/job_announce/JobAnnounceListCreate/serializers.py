from rest_framework.serializers import ModelSerializer

from apps.job.models import JobAnnounce


class JobAnnounceListCreateSerializer(ModelSerializer):

    class Meta:
        model = JobAnnounce
        fields = (
            "id",
            "title",
            "body",
            "job_type",
            "price",
            "price_measure",
            "level",
            "technology",
            "profession",
            "location",
        )
