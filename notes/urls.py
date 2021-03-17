from django.contrib import admin
from django.urls import path
from .views import NoteListView,NoteView,NoteDownloadView

urlpatterns = [
    path('notes/', NoteListView.as_view()),
    path('notes/download/', NoteDownloadView.as_view()),
    path('notes/<slug:slug_url>/', NoteView.as_view()),
]