from rest_framework import serializers

from .models import Note

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ("text", "type_of_text",)


class NoteDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ("text", "author", "type_of_text",)
