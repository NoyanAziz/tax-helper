from django.urls import path

from .views import UploadAttachmentView


urlpatterns = [
    path('upload-attachment/', UploadAttachmentView.as_view(),
         name='upload_attachment')
]
