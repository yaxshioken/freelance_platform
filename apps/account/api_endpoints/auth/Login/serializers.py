from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework.fields import CharField
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class LoginSerializer(TokenObtainPairSerializer):
    phone = PhoneNumberField()
    password = CharField()

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # token['name'] = user.name
        return token
