from django.core.cache import cache
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView, set_rollback

from apps.account.api_endpoints.activation.VerificationCode.serializers import \
    VerificationSerializer
from apps.account.models import Account


class VerificationCodeView(APIView):
    @swagger_auto_schema(request_body=VerificationSerializer)
    def post(self, request):
        serializer = VerificationSerializer(data=request.data)
        if serializer.is_valid():
            phone = str(serializer.validated_data["phone"])
            code = cache.get(phone)
            if not code:
                raise ValidationError(
                    detail="Your code has beem expired please try again", code="phone"
                )
            else:
                if code == int(serializer.validated_data["code"]):
                    account = get_object_or_404(Account, phone=phone)
                    account.is_active = True
                    account.save()
                    return Response(
                        data="Your account activated", status=status.HTTP_202_ACCEPTED
                    )
                else:
                    raise ValidationError(detail="Your code is wrong", code="code")

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


__all__ = ("VerificationCodeView",)
