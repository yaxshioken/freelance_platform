from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import Serializer

from apps.account.models import Account


class SendActivationCodeSerializer(Serializer):
    phone = PhoneNumberField(region="UZ")

    def validate_phone(self, phone):
        if not Account.objects.filter(phone=phone).exists():
            raise ValidationError(detail=f"with {phone} user not found", code="phone")
        return phone
