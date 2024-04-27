from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

from .param_validations import LoginParams


class LoginView(APIView):
    """Login View """

    def post(self, request):
        """
        Post method for LoginView

        :param request:
        :return:
        """
        validator = LoginParams(data=request.data)
        validator.is_valid(raise_exception=True)

        email = validator.validated_data.get("email")
        password = validator.validated_data.get("password")

        user = authenticate(email=email, password=password)
        if not user:
            return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

        refresh = RefreshToken.for_user(user)

        response_date = {
            "refresh": str(refresh),
            "access": str(refresh.access_token)
        }

        return Response(response_date)
