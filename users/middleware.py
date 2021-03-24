from django.conf import settings

from .models import User
from .services import decode_auth_token
from rest_framework import authentication
from rest_framework import exceptions


class AuthClass(authentication.BaseAuthentication):
    def authenticate(self, request):
        if (not (any(request.path.startswith(url) for url in settings.WHITE_LIST))):
            try:
                user = User.objects.get(login=decode_auth_token(request.headers[settings.TOKEN_HEADER]))
                user.is_active = True
                user.is_authenticated = True
                return (user,None)
            except BaseException:
                raise exceptions.NotAuthenticated('You are not auth')