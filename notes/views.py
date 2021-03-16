from rest_framework import generics

from .models import Note
from .serializers import NoteSerializer,NoteDetailSerializer


# Create your views here.

class NoteListView(generics.ListAPIView, generics.CreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class NoteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NoteDetailSerializer

    def get_object(self):
        url_slug = self.kwargs['slug_url']
        notes = Note.objects.get(slug_address=url_slug)
        return notes