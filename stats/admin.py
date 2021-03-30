from django.contrib import admin
from .models import Stats
from .tasks import create_statistic
# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['name', 'result','date']
    ordering = ['date']
    actions = ['statistic_report']

admin.site.register(Stats, ArticleAdmin)
