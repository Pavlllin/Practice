
from rest_framework import generics
from rest_framework.response import Response

from .models import User
from .serializers import UserRegisterSerializer, UserLoginSerializer
from .services import encode_auth_token,check_user

from django.conf import settings

# Create your views here
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
                serializer.save()
                auth_token = encode_auth_token(serializer.data["login"])
                res_dict = {"res": "Успешный вход", "token": auth_token}
                response = Response(data=res_dict, status=201)
                return response
        else:
            ans = "Неправильный логин или пароль"
            return Response(data=ans, status=400)


class LoginView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserLoginSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            return check_user(serializer)


