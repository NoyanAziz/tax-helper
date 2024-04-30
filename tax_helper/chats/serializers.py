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

    attachment = serializers.FileField(
        source='message_attachment.attachment', required=False)
    person_name = serializers.CharField(
        source='user.full_name', required=False)

    class Meta:
        """Meta class of MessagePromptSerializer."""

        model = MessagePrompt
        fields = ('id', 'message', 'user', 'role', 'attachment', 'person_name')
        read_only_fields = ('id',)
