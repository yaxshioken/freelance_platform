from apps.technology.api_endpoints.profession import serializers
from apps.technology.models import Technology


class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = ("id", "name")
        read_only_fields = [
            "id",
            "slug",
        ]
