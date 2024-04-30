from django.urls import path

from .views import UploadAttachmentView, MessagePromptView, MessagePromptListView


urlpatterns = [
    path('upload-attachment/', UploadAttachmentView.as_view(),
         name='upload_attachment'),
    path('send-prompt/', MessagePromptView.as_view(),
         name='send_prompt'),
    path('prompts/', MessagePromptListView.as_view(), name='prompts'),
]
