from phonenumber_field.modelfields import PhoneNumberField
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer

from apps.account.models import Account, AccountInfo


class RegisterSerializer(serializers.ModelSerializer):
    password = CharField(write_only=True)
    password2 = CharField(write_only=True)
    phone = PhoneNumberField(region="uz")

    class Meta:
        model = Account
        fields = ("id", "first_name", "last_name", "phone", "password", "password2")

    def validate_phone(self, phone):
        if Account.objects.filter(phone=phone).exists():
            raise ValidationError(detail="This phone already registered", code="phone")
        return phone

    def create(self, validated_data):
        account = Account.objects.create(
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            phone=str(validated_data["phone"]),
        )
        account.set_password(validated_data["password"])
        account.save()
        return account

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise ValidationError(detail="Passwords must be match", code="password")

        return attrs


class AccountInfoSerializer(ModelSerializer):
    class Meta:
        model = AccountInfo
        fields = "__all__"
