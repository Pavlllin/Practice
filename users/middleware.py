from django.conf import settings
from django.http import JsonResponse
from rest_framework import status

from .models import User
from .services import decode_auth_token


class AuthMiddleware():
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        if (not (any(request.path.startswith(url) for url in settings.WHITE_LIST))):
            print("Success")
            try:
                request.User = User.objects.get(login=decode_auth_token(request.headers[settings.TOKEN_HEADER]))
                response = self.get_response(request)
                return response
            except Exception:
                return JsonResponse({'error': "You are not auth"}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            response = self.get_response(request)
            return response