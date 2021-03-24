from rest_framework import permissions


class NotePermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
            noteauthor = obj.author
            print(noteauthor)
            print(request.user)
            if request.user == noteauthor:
                return True
            else:
                return False