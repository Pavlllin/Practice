from django.db import models

# Create your models here.
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


class TypeStats(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=50,unique=True)

#Сколько пользоватей за день создался
#Сколько txt файлов за день создалось
#Сколько py файлов за день создалось
#Сколько cpp файлов за день создалось
#кол-во постов где длина содержания больше 500 символов за день