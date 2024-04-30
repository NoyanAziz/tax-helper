from rest_framework import serializers

from .constants import USER
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
    sender = serializers.SerializerMethodField()

    class Meta:
        """Meta class of MessagePromptSerializer."""

        model = MessagePrompt
        fields = ('id', 'message', 'user', 'role', 'attachment', 'sender')
        read_only_fields = ('id',)

    def get_sender(self, instance):
        """
        Get sender.

        :param instance:
        :return:
        """
        return "You" if instance.role == USER else 'Tax Helper'
