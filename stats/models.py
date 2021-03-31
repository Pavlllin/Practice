from django.db import models
from pastebin.decorator import RouterDecorator
# Create your models here.


@RouterDecorator()
class Stats(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя статистики")
    result = models.IntegerField(verbose_name="Результат статистики")
    date = models.DateTimeField(auto_now_add=True,verbose_name="Создана в ")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Статистика"
        verbose_name_plural = "Статистика"
        db_table = "Stats"

@RouterDecorator()
class TypeStats(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=50,unique=True)
