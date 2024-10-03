from django.urls import path

from apps import technology
from apps.technology.api_endpoints.profession.views import \
    ProfessionListCreateView
from apps.technology.api_endpoints.technology.views import \
    TechnologyListCreateView

urlpatterns = [
    path("", TechnologyListCreateView.as_view(), name="technology"),
    path("profession/", ProfessionListCreateView.as_view(), name="profession"),
]
