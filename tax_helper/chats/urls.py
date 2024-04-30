from django.urls import path

from .views import MessagePromptView, MessagePromptListView


urlpatterns = [
    path('send-prompt/', MessagePromptView.as_view(),
         name='send_prompt'),
    path('prompts/', MessagePromptListView.as_view(), name='prompts'),
]
