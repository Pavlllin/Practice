import csv

from typing.io import TextIO
from users.models import User

from .models import Type
from .serializers import NoteSerializer


def upload_csv_from_file(file_csv: TextIO, user: User):
    reader = csv.reader(file_csv)
    for row in reader:
        notes_dict = {
            "text": row[0],
            "type_of_text": Type.objects.get(name_of_type=row[1]).pk,
        }
        serializer = NoteSerializer(data=notes_dict)
        serializer.is_valid(raise_exception=True)
        serializer.save(author=user)
