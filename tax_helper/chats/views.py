import os
from groq import Groq
from django.http import StreamingHttpResponse
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from .models import MessageAttachment, MessagePrompt
from .serializers import MessageAttachmentSerializer, MessagePromptSerializer


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


def stream_response(response):
    for chunk in response:
        text = chunk.choices[0].delta.content
        yield text


class MessagePromptView(APIView):
    """MessagePromptView class."""

    def post(self, request, *args, **kwargs):
        """
        Get all message prompts.
        """
        requester = request.user
        request_data = {
            **request.data,
            "user": request.user.id
        }

        serializer = MessagePromptSerializer(data=request_data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)

        old_messages = MessagePrompt.objects.filter(user=requester)
        message_prompts = [
            {
                "role": "system",
                "content": "You are a tax helper, you will answer questions related to taxes."
            },
        ] + [
            {"role": "user", "content": message.message}
            for message in old_messages
        ]

        client = Groq(api_key=os.environ.get("GROQ_API_KEY"),)
        stream = client.chat.completions.create(
            messages=message_prompts,
            model="mixtral-8x7b-32768",
            temperature=0.5,
            max_tokens=1024,
            top_p=1,
            stop=None,
            stream=True,
        )

        return StreamingHttpResponse(stream_response(stream))


class MessagePromptListView(ListAPIView):
    """List message prompts."""

    serializer_class = MessagePromptSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """
        Get all message prompts.

        :return:
        """
        return MessagePrompt.objects.filter(user=self.request.user)
