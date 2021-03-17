from django.contrib import admin
from .models import User
# Register your models here.



def note_report(queryset):

    queryset.update(status='p')

note_report.short_description = "Отчет по всем записям пользователей"

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['login', 'name']
    ordering = ['login']
    actions = [note_report]

admin.site.register(User, ArticleAdmin)

