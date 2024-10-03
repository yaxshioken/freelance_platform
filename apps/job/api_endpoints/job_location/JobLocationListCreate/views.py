from rest_framework.generics import ListCreateAPIView

from apps.job.api_endpoints.job_location.JobLocationListCreate.serializers import \
    JobLocationListCreateSerializer
from apps.job.models import JobLocation


class JobLocationListCreateView(ListCreateAPIView):
    queryset = JobLocation.objects.all()
    serializer_class = JobLocationListCreateSerializer


__all__ = ("JobLocationListCreateView",)
