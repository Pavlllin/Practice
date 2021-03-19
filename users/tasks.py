from celery import shared_task
from datetime import datetime
from .models import User
import csv

@shared_task()
def create_report(user_ids = None):
    with open('content/report' + str(datetime.now().strftime("%m_%d_%Y_%H_%M_%S")) + ".csv", 'w', newline='',
              encoding='utf-8') as file:
        csv_file = csv.writer(file, delimiter=',')
        csv_file.writerow(["Логин", "Текст записи", "Адрес записи", "Тип записи"])
        if(user_ids is None):
            queryset = User.objects.all()
        else:
            queryset = User.objects.filter(pk__in=user_ids)
        queryset = queryset.prefetch_related("note_author__type_of_text").values('note_author__text',
                                                                                 'note_author__slug_address',
                                                                                 'note_author__type_of_text', 'login')
        for user in queryset:
            csv_file.writerow([user['login'], user['note_author__text'], user['note_author__slug_address'],
                               user['note_author__type_of_text']])