from django.contrib import admin
from django.urls import path
from .views import NoteListView,NoteView,NoteDownloadView,UploadNotesCSV

urlpatterns = [
    path('notes/', NoteListView.as_view()),
    path('notes/(?P<text>)\w/', NoteListView.as_view()),
    path('notes/download/', NoteDownloadView.as_view()),
    path('notes/uploadcsv/', UploadNotesCSV.as_view()),
    path('notes/<slug:slug_url>/', NoteView.as_view()),
]