from django.contrib.auth import forms

from .models import User


class UserCreationForm(forms.UserCreationForm):
    """A form for creating new users. Includes all the required."""

    class Meta:
        """Meta class for CustomUserCreationForm."""

        model = User
        fields = ("email",)


class UserChangeForm(forms.UserChangeForm):
    """A form for updating users. Includes all the fields on."""

    class Meta:
        """Meta class for CustomUserChangeForm."""

        model = User
        fields = ("email",)
