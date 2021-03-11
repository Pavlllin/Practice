from rest_framework import generics
from rest_framework.response import Response
from .models import User
from .serializers import UserRegisterSerializer,UserLoginSerializer
from django.contrib.auth.hashers import make_password


# Create your views here
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer


class LoginView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserLoginSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            print(serializer.data["login"])
            Users = User.objects.filter(login = serializer.data["login"],password = make_password(serializer.data["password"],salt = "secret_salt"))
            if Users.first() is not None:
                ans = "Успешный вход"
                return Response(data=ans, status=201)
            else:
                ans = "Неправильный логин или пароль"
                return Response(data=ans, status=400)