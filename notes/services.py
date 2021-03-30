import csv
from datetime import datetime

from django.db.models.functions import Length
from stats.models import Stats
from users.models import User

from .models import Type, Note
from .serializers import NoteSerializer


def upload_csv_from_file(path: str, user: str):
    with open(path) as file:
        reader = csv.reader(file)
        user = User.objects.get(login=user)
        for row in reader:
            notes_dict = {
                "text": row[0],
                "type_of_text": row[1],
                "author": user.pk
            }
            serializer = NoteSerializer(data=notes_dict)
            serializer.is_valid(raise_exception=True)
            serializer.save(author=user)


def create_csv_file(file_csv):
    path = 'content/csv_file' + str(datetime.now().strftime("%m_%d_%Y_%H_%M_%S")) + ".csv"
    with open(path, 'w', newline='',
              encoding='utf-8') as file:
        reader = csv.reader(file_csv)
        csv_file = csv.writer(file, delimiter=',')
        for row in reader:
            csv_file.writerow([row[0], Type.objects.get(name_of_type=row[1]).pk])

        return path


def create_stat_notes(type, len_post=None):
    today = datetime.now()
    if len_post is None:
        result = Note.objects.filter(date__year=today.year, date__month=today.month, date__day=today.day,
                                     type_of_text__name_of_type=type)
        Stats(name="Кол-во записей с типом " + type + " было создано", result=result.count()).save()
    else:
        result = Note.objects.annotate(text_len=Length('text')).filter(date__year=today.year, date__month=today.month,
                                                                       date__day=today.day,
                                                                       type_of_text__name_of_type=type,
                                                                       text_len__gt=len_post)
        Stats(name="Кол-во записей с типом " + type + " было создано, где длина текста больше " + str(len_post),
              result=result.count()).save()
