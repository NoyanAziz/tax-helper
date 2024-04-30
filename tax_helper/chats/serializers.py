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

    attachment = serializers.FileField(source='message_attachment.attachment')
    user = serializers.CharField(source='user.full_name')

    class Meta:
        """Meta class of MessagePromptSerializer."""

        model = MessagePrompt
        fields = ('id', 'message', 'user', 'attachment')
