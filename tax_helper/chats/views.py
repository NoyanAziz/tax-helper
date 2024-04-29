from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import MessageAttachment
from .serializers import MessageAttachmentSerializer


class UploadAttachmentView(CreateAPIView):
    """UploadAttachmentView class."""

    serializer_class = MessageAttachmentSerializer
    permission_classes = (IsAuthenticated,)
    queryset = MessageAttachment.objects.all()

    def create(self, request, *args, **kwargs):
        """
        Create a new message attachment.

        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        request.data['uploaded_by'] = request.user.id
        request.data['name'] = request.FILES['attachment'].name

        return super().create(request, *args, **kwargs)
