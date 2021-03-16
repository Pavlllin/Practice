
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from .models import User
from .serializers import UserRegisterSerializer, UserLoginSerializer
from .services import encode_auth_token, check_user, UserData


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
                response = Response(data=res_dict, status=status.HTTP_200_OK)
                return response
        else:
            ans_dict = {"res": "Неправильный логин или пароль"}
            return Response(data=ans_dict, status=status.HTTP_400_BAD_REQUEST)


class LoginView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserLoginSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user_data = UserData(login=serializer.data["login"], password=serializer.data["password"])
            check_result = check_user(user_data)
            res_dict = {"ans": check_result.ans, "token": check_result.token}
            response = Response(data=res_dict, status=check_result.status)
            return response
