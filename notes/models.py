from django.db import models


# Create your models here.
class Note(models.Model):
    text = models.CharField(max_length=500,
                            verbose_name="Текст записи")
    author = models.ForeignKey('notes.User', on_delete=models.CASCADE,
                               verbose_name="Автор записи")


class User(models.Model):
    name = models.CharField(max_length=100,
                            verbose_name="Имя пользователя")
    login = models.CharField(max_length=100,
                             verbose_name="Логин")
    password = models.CharField(max_length=100,
                                verbose_name="Пароль")
