from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField
from rest_framework.serializers import Serializer

from apps.account.models import Account


class VerificationSerializer(Serializer):
    phone = PhoneNumberField(region="UZ")
    code = CharField()

    def validate_code(self, code):
        if len(code) != 4:
            raise ValidationError(detail="Code lenght must be 4", code="code")
        return code

    def validate_phone(self, phone):
        if not Account.objects.filter(phone=phone).exists():
            raise ValidationError(detail=f"with {phone} user not found", code="phone")
        return phone
