from django.http import HttpResponse
from django.http import JsonResponse
from .models import User
from .services import decode_auth_token
from pastebin.settings import WHITE_LIST
from rest_framework.response import Response

class SimpleMiddleware():
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        response = self.get_response(request)
        if(not(any(request.path.startswith(url) for url in WHITE_LIST))):
            print("Success")
            try:
                response.user = User.objects.get(login=decode_auth_token(request.headers["X-Auntification"]))
                return response
            except Exception:
                return JsonResponse({'error': "You are not auth"}, status=401)
        else:
            return response