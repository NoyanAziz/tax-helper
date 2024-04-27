from rest_framework import serializers


class LoginParams(serializers.Serializer):
    """Param validations for LoginView."""

    email = serializers.EmailField()
    password = serializers.CharField()
