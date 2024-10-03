from select import select

from django.contrib.postgres.search import TrigramSimilarity
from django.db.models import Q
from rest_framework.generics import ListCreateAPIView

from apps.job.api_endpoints.job_announce.JobAnnounceListCreate.serializers import \
    JobAnnounceListCreateSerializer
from apps.job.models import JobAnnounce


class JobAnnounceListCreateView(ListCreateAPIView):
    queryset = JobAnnounce.objects.all()
    serializer_class = JobAnnounceListCreateSerializer

    def get_queryset(self):
        query = self.request.query_params.get("search", None)
        queryset = super().get_queryset()

        if query:
            queryset = queryset.filter(
                Q(body__icontains=query) | Q(title__icontains=query)
            )
        price_from = self.request.query_params.get("price_from", None)
        price_to = self.request.query_params.get("price_to", None)

        if price_from and price_to:
            return JobAnnounce.objects.filter(
                price__gte=price_from, price__lte=price_to
            )
        return queryset

    def filter_queryset(self, request):
        level = self.request.query_params.get("level", None)
        technologies = self.request.query_params.get("technologies", None)
        price_measure = self.request.query_params.get("price_measure", None)
        payment_verified = self.request.query_params.get("payment_verified", None)
        job_type = self.request.query_params.get("job_type", None)
        profession = self.request.query_params.get("profession", None)
        if level:
            return JobAnnounce.objects.filter(level=level)
        if technologies:
            return JobAnnounce.objects.filter(technologies=technologies)
        if price_measure:
            return JobAnnounce.objects.filter(price_measure=price_measure)
        if payment_verified:
            return JobAnnounce.objects.filter(payment_verified=payment_verified)
        if job_type:
            return JobAnnounce.objects.filter(job_type=job_type)
        if profession:
            return JobAnnounce.objects.filter(profession=profession)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


__all__ = ("JobAnnounceListCreateView",)
