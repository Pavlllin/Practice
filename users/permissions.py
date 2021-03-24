from rest_framework import permissions
from notes.views import  NoteView


class NotePermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
         if view == NoteView:
            noteauthor = obj.author__login
            if request.user == noteauthor:
                return True
            else:
                return False