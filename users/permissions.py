from rest_framework import permissions


class NotePermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
            noteauthor = obj.author
            if request.user == noteauthor:
                return True
            else:
                return False