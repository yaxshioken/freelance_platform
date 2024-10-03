from django.db.models import Q
from rest_framework import generics

from apps.job.api_endpoints.job_technology.serializers import \
    JobTechnologyListCreateSerializer
from apps.job.models import JobTechnology


class JobTechnologyListCreateView(generics.ListCreateAPIView):
    queryset = JobTechnology.objects.all()
    serializer_class = JobTechnologyListCreateSerializer

    def get_queryset(self):
        query = self.request.query_params.get("search", None)
        queryset = super().get_queryset()
        city = self.request.query_params.get("city", None)
        country = self.request.query_params.get("country", None)
        if city:
            return queryset.filter(city__icontains=city)
        if country:
            return queryset.filter(country__icontains=country)
        if query:
            queryset = queryset.filter(
                Q(body__icontains=query) | Q(title__icontains=query)
            )

        return queryset
