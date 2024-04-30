from django.db import models

from .constants import PROMPT_ROLE_CHOICES
from .utils import attachment_uploading_path


class CustomTimeStampModel(models.Model):
    """Custom Timestamp model with is_active status."""

    is_active = models.BooleanField(db_index=True, default=True)
    created_at = models.DateTimeField(db_index=True, auto_now_add=True)
    modified_at = models.DateTimeField(db_index=True, auto_now=True)

    class Meta:
        """Meta for custom timestamp model."""

        abstract = True


class MessagePrompt(CustomTimeStampModel):
    """MessagePrompt model."""

    user = models.ForeignKey(
        'users.User', related_name='message_prompts', on_delete=models.CASCADE)
    role = models.IntegerField(choices=PROMPT_ROLE_CHOICES)
    message = models.TextField()

    class Meta:
        """Meta class."""

        app_label = 'chats'
        db_table = 'message_prompt'
        verbose_name = 'Message Prompt'
        verbose_name_plural = 'Message Prompts'

    def __str__(self):
        """
        Return the string representation of this class's objects.

        :return: return message
        """
        return self.message


class MessageAttachment(CustomTimeStampModel):
    """MessageAttachment model class."""

    uploaded_by = models.ForeignKey(
        'users.User', null=True, blank=True, on_delete=models.CASCADE)
    message = models.OneToOneField(
        'MessagePrompt', null=True, blank=True, related_name='message_attachment', on_delete=models.CASCADE)

    name = models.CharField(max_length=200, blank=True, null=True)
    attachment = models.FileField(upload_to=attachment_uploading_path)

    class Meta:
        """Meta class of MessageAttachment."""

        app_label = 'chats'
        db_table = 'message_attachment'
        verbose_name_plural = 'Message Attachments'

    def __str__(self):
        """
        Return the string representation of this class's objects.

        :return: return attachment file name
        """
        return self.name if self.name else ''
