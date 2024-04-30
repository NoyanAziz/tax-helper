from __future__ import absolute_import

from celery import shared_task


from .constants import SYSTEM, USER
from users.models import User

from .utils import perform_ocr
from .models import MessageAttachment, MessagePrompt


@shared_task
def save_converted_message_prompt_task(file_path, user_id, attachment_id):
    """
    Save converted message prompt.

    :param message_attachment:
    :return:
    """
    if not file_path or not user_id:
        return

    user = User.objects.get(pk=user_id)

    message = perform_ocr(file_path)

    created_message = MessagePrompt.objects.create(
        user=user, role=USER, message=message)

    attachment = MessageAttachment.objects.get(pk=attachment_id)
    attachment.message = created_message
    attachment.save()


@shared_task
def add_system_prompt(prompt, user_id):
    """
    Save converted message prompt.

    :param message_attachment:
    :return:
    """
    user = User.objects.get(pk=user_id)
    MessagePrompt.objects.create(user=user, role=SYSTEM, message=prompt)
