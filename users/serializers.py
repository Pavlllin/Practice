from django.conf import settings
from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from .models import User


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("name", "login", "password")

    def create(self, validated_data):
        user = User(
            name=validated_data['name'],
            login=validated_data['login'],
            password=make_password(validated_data['password'], salt=settings.SALT)
        )
        user.save()
        return user


class UserLoginSerializer(serializers.ModelSerializer):
    login = serializers.CharField(max_length=100)

    class Meta:
        model = User
        fields = ("login","password")