from django.shortcuts import redirect

from .models import User
from .services import decode_auth_token
from pastebin.settings import BLACK_LIST

class SimpleMiddleware():
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        response = self.get_response(request)
        if(request.path in BLACK_LIST):
            print("Success")
            try:
                response.user = User.objects.get(login=decode_auth_token(request.headers["X-Auntification"]))
                return response
            except Exception:
                return redirect("/api/login/")
        else:
            return response