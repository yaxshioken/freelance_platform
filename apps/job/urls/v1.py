from django.urls import path

from apps.job.api_endpoints import job_announce, job_location, job_technology
from apps.job.api_endpoints.job_technology.views import JobTechnologyListCreateView

urlpatterns = [
    path("job-announce/", job_announce.JobAnnounceListCreateView.as_view(), name="job"),
    path(
        "job-location/",
        job_location.JobLocationListCreateView.as_view(),
        name="job-location",
    ),
    path('job-technologies/',JobTechnologyListCreateView.as_view(), name="job-technology"),

]
