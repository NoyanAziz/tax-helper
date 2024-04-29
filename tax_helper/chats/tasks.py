from __future__ import absolute_import

from celery import shared_task


from users.models import User

from .utils import perform_ocr
from .models import MessagePrompt


@shared_task
def save_converted_message_prompt_task(file_path, user_id):
    """
    Save converted message prompt.

    :param message_attachment:
    :return:
    """
    if not file_path or not user_id:
        return

    user = User.objects.get(pk=user_id)

    message = perform_ocr(file_path)
    MessagePrompt.objects.create(user=user, message=message)
