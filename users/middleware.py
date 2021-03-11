from .models import User
import jwt

class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)
#        request.user = User.object.get(pk=jwt['user_id'])
        # Code to be executed for each request/response after
        # the view is called.

        return response