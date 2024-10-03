from rest_framework.serializers import ModelSerializer

from apps.technology.models import Profession


class ProfessionSerializer(ModelSerializer):
    class Meta:
        model = Profession
        fields = ("id", "name")
        read_only_fields = ("id", "slug")
