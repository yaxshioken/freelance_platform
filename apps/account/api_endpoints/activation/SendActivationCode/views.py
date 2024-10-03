from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.account.api_endpoints.activation.SendActivationCode.serializers import \
    SendActivationCodeSerializer
from apps.account.tasks import send_activation_code


class SendActivationCodeView(APIView):
    @swagger_auto_schema(request_body=SendActivationCodeSerializer)
    def post(self, request):
        serializer = SendActivationCodeSerializer(data=request.data)
        if serializer.is_valid():
            send_activation_code.delay(phone=str(serializer.validated_data["phone"]))
            return Response("activation code has beem sent", status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


__all__ = ("SendActivationCodeView",)
