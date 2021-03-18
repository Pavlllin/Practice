
from django.contrib import admin

from .models import User
from .services import create_report


# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['login', 'name']
    ordering = ['login']
    actions = ['note_report']

    def note_report(self, request, queryset):
        create_report(queryset)

    note_report.short_description = "Отчет по всем записям пользователей"

admin.site.register(User, ArticleAdmin)

