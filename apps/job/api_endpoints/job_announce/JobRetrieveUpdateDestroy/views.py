from rest_framework.generics import RetrieveUpdateDestroyAPIView

from apps.job.api_endpoints.job_announce.JobRetrieveUpdateDestroy.serializers import JobRetrieveUpdateDestroySerializer
from apps.job.models import JobAnnounce


class JobRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = JobRetrieveUpdateDestroySerializer
    queryset =JobAnnounce.objects.all()
