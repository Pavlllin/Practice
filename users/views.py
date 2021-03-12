from django.contrib.auth.hashers import make_password
from rest_framework import generics
from rest_framework.response import Response

from .models import User
from .serializers import UserRegisterSerializer, UserLoginSerializer
from .services import encode_auth_token

from pastebin.settings import salt

# Create your views here
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
                ans = "Успешная регистрация"
                response = Response(data=ans, status=201)
                response["X-Auntification"] = encode_auth_token(serializer.data["login"])
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

            Users = User.objects.filter(login=serializer.data["login"],
                                        password=make_password(serializer.data["password"],
                                                               salt=salt))
            if Users.first() is not None:
                ans = "Успешный вход"
                auth_token = encode_auth_token(serializer.data["login"])
                res_dict = {"res":"Успешный вход","X-Auntification":auth_token}
                response = Response(data=res_dict,status=201)
                return response
            else:
                ans = "Неправильный логин или пароль"
                return Response(data=ans, status=400)

