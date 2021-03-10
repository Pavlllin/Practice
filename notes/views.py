from rest_framework import generics

from .models import User, Note
from .serializers import UserSerializer, NoteSerializer


# Create your views here.

# class UserListView(generics.ListAPIView, generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

#Работа с моделью (удаление, пут, создание, получение)

class NoteListView(generics.ListAPIView, generics.CreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
