from .models import User
import jwt
from .services import decode_auth_token

class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        response = self.get_response(request)
        response.user = User.object.get(login=decode_auth_token(request.headers["X-Auntification"]))
        return response