from django.contrib import admin

from .models import MessageAttachment, MessagePrompt


class MessageAttachmentAdmin(admin.ModelAdmin):
    """MessageAttachmentAdmin class."""

    list_display = ('name', 'message', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name',)


class MessagePromptAdmin(admin.ModelAdmin):
    """MessagePromptAdmin class."""

    list_display = ('user', 'message', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('message',)


admin.site.register(MessageAttachment, MessageAttachmentAdmin)
admin.site.register(MessagePrompt, MessagePromptAdmin)
