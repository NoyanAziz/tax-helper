import os

from django.http import StreamingHttpResponse
from groq import Groq
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from .tasks import add_system_prompt
from .constants import USER
from .models import MessagePrompt
from .serializers import MessageAttachmentSerializer, MessagePromptSerializer


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
        requester_id = request.user.id

        attachment = request.FILES.get('attachment')
        if attachment:
            request_data = {
                'attachment': attachment,
                'uploaded_by': requester_id,
                'name': attachment.name
            }

            serializer = MessageAttachmentSerializer(data=request_data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response(status=status.HTTP_201_CREATED)
        else:
            request_data = {
                'message': request.POST.get('message'),
                'user': requester_id,
                'role': USER
            }

            serializer = MessagePromptSerializer(data=request_data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            old_messages = MessagePrompt.objects.filter(
                user_id=requester_id).order_by('created_at')
            message_prompts = [{
                "role": "user",
                "content": "You are a tax helper, you will answer questions related to taxes. Do not display the social security number from W2 data ever."
            }] + [
                {
                    "role": "user" if message.role == USER else "system",
                    "content": message.message
                }
                for message in old_messages
            ]

            try:
                client = Groq(api_key=os.environ.get("GROQ_API_KEY"),)
                stream = client.chat.completions.create(
                    messages=message_prompts,
                    model="gemma-7b-it",
                    temperature=0.5,
                    max_tokens=1024,
                    top_p=1,
                    stop=None,
                    stream=False,
                )

                response_data = stream.choices[0].message.content
                add_system_prompt.delay(response_data, requester_id)
            except Exception:
                response_data = "An error occurred. Please try again later."

            return Response(response_data)


class MessagePromptListView(ListAPIView):
    """List message prompts."""

    serializer_class = MessagePromptSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """
        Get all message prompts.

        :return:
        """
        return MessagePrompt.objects.filter(user=self.request.user).order_by('created_at')
