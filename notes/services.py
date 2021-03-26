import csv
from datetime import datetime

from users.models import User

from .models import Type
from .serializers import NoteSerializer


def upload_csv_from_file(path: str, user: User):
    with open(path) as file:
        reader = csv.reader(file)
        for row in reader:
            notes_dict = {
                "text": row[0],
                "type_of_text": row[1],
            }
            serializer = NoteSerializer(data=notes_dict)
            serializer.is_valid(raise_exception=True)
            serializer.save(author=user)


def create_csv_file(file_csv):
    with open('content/csv_file' + str(datetime.now().strftime("%m_%d_%Y_%H_%M_%S")) + ".csv", 'w', newline='',
              encoding='utf-8') as file:
        reader = csv.reader(file_csv)
        csv_file = csv.writer(file, delimiter=',')
        for row in reader:
            csv_file.writerow([row[0],Type.objects.get(name_of_type=row[1]).pk])
        path = 'content/csv_file' + str(datetime.now().strftime("%m_%d_%Y_%H_%M_%S")) + ".csv"
        return path