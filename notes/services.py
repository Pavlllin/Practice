import csv
from datetime import datetime
from typing import Optional

from django.db.models import Count
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
                "title": row[0],
                "text": row[1],
                "type_of_text": row[2],
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
            csv_file.writerow([row[0],row[1], Type.objects.get(name_of_type=row[2]).pk])

        return path


def create_stat_notes(len_post: Optional[int] = None):
    today = datetime.now()
    if len_post is None:
        result = Note.objects.filter(date__year=today.year, date__month=today.month, date__day=today.day).values(
            'type_of_text__name_of_type').annotate(
            num_notes=Count("text")).values('type_of_text__name_of_type', 'num_notes')
        for item in result:
            Stats(name="Кол-во записей с типом " + item['type_of_text__name_of_type'] + " было создано",
                  result=item['num_notes']).save()
    else:
        result = Note.objects.annotate(text_len=Length('text')).filter(date__year=today.year, date__month=today.month,
                                                                       date__day=today.day,
                                                                       text_len__gt=len_post).values(
            'type_of_text__name_of_type').annotate(num_notes=Count("text")).values('type_of_text__name_of_type',
                                                                                   'num_notes')
        for item in result:
            Stats(name="Кол-во записей с типом " + item[
                'type_of_text__name_of_type'] + " было создано, где длина текста больше " + str(len_post),
                  result=item['num_notes']).save()
