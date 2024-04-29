from django.contrib import admin

from .models import MessageAttachment


class MessageAttachmentAdmin(admin.ModelAdmin):
    """MessageAttachmentAdmin class."""

    list_display = ['name', 'message', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name']


admin.site.register(MessageAttachment, MessageAttachmentAdmin)
