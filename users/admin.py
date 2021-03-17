import csv
from datetime import datetime

from django.contrib import admin

from .models import User


# Register your models here.


def note_report(modeladmin, request, queryset):
    with open('content/report' + str(datetime.now().strftime("%m_%d_%Y_%H_%M_%S")) + ".csv", 'w', newline='',
              encoding='utf-8') as file:
        csv_file = csv.writer(file, delimiter=',')
        csv_file.writerow(["Логин", "Текст записи", "Адрес записи", "Тип записи"])
        # queryset = queryset.prefetch_related("note_author__type_of_text")
        # print("foo")
        # for user in queryset:
        #     for u in user.note_author.all():
        #         csv_file.writerow([user.login, u.text, u.slug_address, u.type_of_text])
        #         print("bar")
        queryset = queryset.prefetch_related("note_author__type_of_text").values('note_author__text',
                                                                                 'note_author__slug_address',
                                                                                 'note_author__type_of_text', 'login')
        for user in queryset:
            csv_file.writerow([user['login'], user['note_author__text'], user['note_author__slug_address'],
                               user['note_author__type_of_text']])

note_report.short_description = "Отчет по всем записям пользователей"

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['login', 'name']
    ordering = ['login']
    actions = [note_report]

admin.site.register(User, ArticleAdmin)

