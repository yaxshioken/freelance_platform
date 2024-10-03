from rest_framework.generics import RetrieveUpdateDestroyAPIView

from apps.job.api_endpoints.job_location.JobLocationRetrieveDestroyUpdate.serializers import \
    JobLocationRetrieveDestroyUpdateSerializer
from apps.job.models import JobLocation


class JobLocationRetrieveDestroyUpdate(RetrieveUpdateDestroyAPIView):
    serializer_class = JobLocationRetrieveDestroyUpdateSerializer
    queryset = JobLocation.objects.all()

