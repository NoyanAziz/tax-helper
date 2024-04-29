from rest_framework import serializers
from .models import MessageAttachment


class MessageAttachmentSerializer(serializers.ModelSerializer):
    """MessageAttachmentSerializer class."""

    class Meta:
        """Meta class of MessageAttachmentSerializer."""

        model = MessageAttachment
        fields = ['id', 'name', 'attachment', 'uploaded_by']
