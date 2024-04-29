from django.apps import AppConfig


class ChatsConfig(AppConfig):
    """ChatsConfig class."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'chats'

    def ready(self):
        """
            Import expenses signals.

            :return:
            """
        import chats.signals  # pylint: disable=unused-import, import-outside-toplevel
