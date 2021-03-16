import datetime

import jwt
from django.conf import settings
from .models import User
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response

def encode_auth_token(user_id:str) -> str:
    """
    Generates the Auth Token
    :return: string
    """
    try:
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=settings.TIME_TOKEN),
            'iat': datetime.datetime.utcnow(),
            'sub': user_id
        }
        return jwt.encode(
            payload,
            settings.PRIVATE_KEY,
            algorithm='RS256'
        )
    except Exception as e:
        return e


def decode_auth_token(auth_token:str) ->str:
    """
    Decodes the auth token
    :param auth_token:
    :return: integer|string
    """
    try:
        payload = jwt.decode(auth_token, settings.PUBLIC_KEY, algorithms=["RS256"])
        return payload['sub']
    except Exception as e:
        return e


def check_user(serializer):
    user = User.objects.filter(login=serializer.data["login"],
                                password=make_password(serializer.data["password"],
                                                       salt=settings.SALT))
    if user.first() is not None:
        auth_token = encode_auth_token(serializer.data["login"])
        res_dict = {"res": "Успешный вход", "token": auth_token}
        response = Response(data=res_dict, status=201)
        return response
    else:
        ans = "Неправильный логин или пароль"
        return Response(data=ans, status=400)