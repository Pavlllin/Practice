import csv
import random
from dataclasses import dataclass
from datetime import datetime
from typing import Optional

import jwt
from django.conf import settings
from django.contrib.auth.hashers import make_password
from notes.models import Note, Type
from rest_framework import status

from .models import User


@dataclass
class UserData:
    login: str
    password: str


@dataclass
class CheckResult:
    token: Optional[str]
    ans: str
    status: str


def encode_auth_token(login: str) -> str:
    """
    Generates the Auth Token
    :return: string
    """
    try:
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=settings.TIME_TOKEN),
            'iat': datetime.datetime.utcnow(),
            'sub': login
        }
        return jwt.encode(
            payload,
            settings.PRIVATE_KEY,
            algorithm='RS256'
        )
    except Exception as e:
        raise e


def decode_auth_token(auth_token: str) -> str:
    """
    Decodes the auth token
    :param auth_token:
    :return: integer|string
    """
    try:
        payload = jwt.decode(auth_token, settings.PUBLIC_KEY, algorithms=["RS256"])
        return payload['sub']
    except Exception as e:
        raise e


def check_user(user_data: UserData) -> CheckResult:
    user = User.objects.filter(login=user_data.login,
                               password=make_password(user_data.password,
                                                      salt=settings.SALT))
    if user.first() is not None:
        auth_token = encode_auth_token(user_data.login)
        check_result = CheckResult(token=auth_token, ans="Успешный вход", status=status.HTTP_200_OK)
        return check_result
    else:
        check_result = CheckResult(token=None, ans="Неправильный логин или пароль", status=status.HTTP_400_BAD_REQUEST)
        return check_result




def create_new_user():
    for i in range(1000, 50000):
        new_user = User(login=i, password=i, name=i)
        new_user.save()


def create_new_note():
    for i in range(1000, 5000):
        for j in range(2, 3):
            new_note = Note(text=i, author=User.objects.get(login=j), slug_address=str(random.randint(0, 10000)),
                            type_of_text=Type.objects.get(type = j-1))
            new_note.save()
