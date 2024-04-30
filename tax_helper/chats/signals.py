"""Contains signals to perform specific actions when a change occur in our database."""

import logging

from django.db.models.signals import post_save
from django.dispatch import receiver

from .tasks import save_converted_message_prompt_task
from .models import MessageAttachment
from .utils import perform_ocr


logger = logging.getLogger(__name__)


@receiver(post_save, sender=MessageAttachment)
def save_converted_message_prompt(sender, instance, created, **kwargs):
    """
    Save converted message prompt.

    :param sender:
    :param instance:
    :param created:
    :param kwargs:
    :return:
    """
    if created:
        save_converted_message_prompt_task.delay(
            instance.attachment.path, instance.uploaded_by.id, instance.id)
