from rest_framework import serializers

from .models import User, Note


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ("text", "author", "type_of_text",)


class NoteDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ("text", "author", "type_of_text",)
