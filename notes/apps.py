from django.apps import AppConfig
from django.db.models.signals import post_save
from .signals import create_slug


class NotesConfig(AppConfig):
    name = 'notes'

    def ready(self):
        from .models import Note
        post_save.connect(create_slug, sender=Note)

