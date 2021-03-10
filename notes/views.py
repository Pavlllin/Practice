from rest_framework import generics

from .models import User, Note
from .serializers import UserSerializer, NoteSerializer,NoteDetailSerializer


# Create your views here.

# class UserListView(generics.ListAPIView, generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

#Работа с моделью (удаление, пут, создание, получение)

class NoteListView(generics.ListAPIView, generics.CreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class NoteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NoteDetailSerializer

    def get_object(self):
        url_slug = self.kwargs['slug_url']
        print(url_slug)
        notes = Note.objects.get(slug_address=url_slug)
        return notes