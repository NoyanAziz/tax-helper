from rest_framework import serializers
from .models import MessageAttachment, MessagePrompt


class MessageAttachmentSerializer(serializers.ModelSerializer):
    """MessageAttachmentSerializer class."""

    class Meta:
        """Meta class of MessageAttachmentSerializer."""

        model = MessageAttachment
        fields = ('id', 'name', 'attachment', 'uploaded_by')


class MessagePromptSerializer(serializers.ModelSerializer):
    """MessagePromptSerializer class."""

    class Meta:
        """Meta class of MessagePromptSerializer."""

        model = MessagePrompt
        fields = ('id', 'message', 'user')
