from django.conf import settings
import pytesseract
from PIL import Image
from pdf2image import convert_from_path


def attachment_uploading_path(instance, filename):
    """
    Return the attachment uploading path of training app.

    :param instance:
    :param filename:
    :return:
    """
    return '{0}/MessageAttachments/{1}/{2}'.format(settings.PROTECTED_MEDIA_URL, instance.uploaded_by.id, filename)


def perform_ocr(attachment):
    """
    Perform OCR on attachment.

    :param attachment:
    :return:
    """
    if attachment.name.lower().endswith('.pdf'):
        images = convert_from_path(attachment)

        text = ''
        for image in images:
            text += pytesseract.image_to_string(image)
    else:
        image = Image.open(attachment)

        text = pytesseract.image_to_string(image)

    return text
