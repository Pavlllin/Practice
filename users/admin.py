
from django.contrib import admin

from .models import User
from .tasks import create_report_task
import json

# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['login', 'name']
    ordering = ['login']
    actions = ['note_report']

    def note_report(self, request, queryset):
        create_report_task.delay(list(queryset.values_list('id',flat = True)))

    note_report.short_description = "Отчет по всем записям пользователей"

admin.site.register(User, ArticleAdmin)

