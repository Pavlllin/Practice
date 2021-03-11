from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password
from .services import encode_auth_token

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("name","login","password")

    def create(self,validated_data):
        user = User(
            name=validated_data['name'],
            login=validated_data['login'],
            password = make_password(validated_data['password'],salt="secret_salt")
        )
        user.save()
        encode_auth_token(validated_data["login"])
        return user


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("login","password")