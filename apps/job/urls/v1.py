from django.urls import path

from apps.job.api_endpoints import job_announce, job_location, job_technology
from apps.job.api_endpoints.job_announce.JobRetrieveUpdateDestroy.views import JobRetrieveUpdateDestroyAPIView
from apps.job.api_endpoints.job_technology.views import JobTechnologyListCreateView

urlpatterns = [
    path("job-announce/", job_announce.JobAnnounceListCreateView.as_view(), name="job"),
    path('job-announce/<pk>',JobRetrieveUpdateDestroyAPIView.as_view(), name="job-detail"),
    path( "job-location/",job_location.JobLocationListCreateView.as_view(),name="job-location"),
    path('job-location/<pk>',job_location.JobLocationRetrieveDestroyUpdate.as_view(), name="job-location-detail"),
    path('job-technologies/', JobTechnologyListCreateView.as_view(), name="job-technology"),

]
