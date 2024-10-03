from django.contrib.postgres.search import TrigramSimilarity
from django.db.models import TextField, Value
from django.db.models.functions import Cast
from rest_framework.generics import ListCreateAPIView

from apps.technology.api_endpoints.profession.serializers import \
    ProfessionSerializer
from apps.technology.models import Profession


class ProfessionListCreateView(ListCreateAPIView):
    queryset = Profession.objects.filter(is_verified=True)
    serializer_class = ProfessionSerializer

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
