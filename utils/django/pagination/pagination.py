from rest_framework import pagination
from rest_framework.response import Response


class CustomPagination(pagination.CursorPagination):
    ordering = '-id'
