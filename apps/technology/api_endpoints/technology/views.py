from django.contrib.postgres.search import TrigramSimilarity
from rest_framework.generics import ListCreateAPIView

from apps.technology.api_endpoints.technology.serializers import \
    TechnologySerializer
from apps.technology.models import Technology


class TechnologyListCreateView(ListCreateAPIView):
    queryset = Technology.objects.filter(is_verified=True)
    serializer_class = TechnologySerializer

    def get_queryset(self):
        query = self.request.query_params.get("search", None)
        queryset = super().get_queryset()

        if query:
            queryset = (
                queryset.annotate(similarity=TrigramSimilarity("name", query))
                .filter(similarity__gt=0.3)
                .order_by("-similarity")
            )

        return queryset
