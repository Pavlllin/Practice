import csv
import io

from django.db.models import Q
from django.http import HttpResponse
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from users.models import User
from users.permissions import NotePermission

from .models import Note
from .serializers import NoteSerializer, NoteDetailSerializer, FileUploadSerializer
from .services import create_csv_file
from .tasks import upload_csv


# Create your views here.


class NoteListView(generics.ListAPIView, generics.CreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=User.objects.get(pk=request.user.pk))
            res_dict = {"res": "Создана новая запись"}
            response = Response(data=res_dict, status=status.HTTP_200_OK)
            return response
        res_dict = {"res": "Не создана новая запись"}
        response = Response(data=res_dict, status=status.HTTP_200_OK)
        return response

    def get_queryset(self):
        text = self.request.query_params.get("text")
        if text is None:
            notes = Note.objects.filter(author__pk=self.request.user.pk)
        else:
            notes = Note.objects.filter(Q(author__pk=self.request.user.pk),
                                        Q(text__contains=text) | Q(title__contains=text))
        return notes


class NoteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NoteDetailSerializer
    permission_classes = [NotePermission]

    def get_object(self):
        url_slug = self.kwargs['slug_url']
        notes = Note.objects.get(slug_address=url_slug)
        self.check_object_permissions(self.request, notes)
        return notes


class UploadNotesCSV(APIView):

    def put(self, request, format=None):
        serializer = FileUploadSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = request.user
        file_csv = serializer.validated_data['file']
        file_csv = io.StringIO(file_csv.read().decode())
        serializer = NoteSerializer()
        path = create_csv_file(file_csv)
        upload_csv.delay(path,str(user))
        res_dict = {"res": "Успешная загрузка"}
        response = Response(data=res_dict, status=status.HTTP_200_OK)
        return response


class NoteDownloadView(APIView):
    def get(self, request):
        notes = Note.objects.filter(author__login=request.user)
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'
        csv_file = csv.writer(response)
        csv_file.writerow(["Текст записи", "Адрес записи", "Тип записи"])
        for n in notes:
            print(n.text, n.slug_address, n.type_of_text)
            csv_file.writerow([n.text, n.slug_address, n.type_of_text])
        return response
