from django.db import models

class User(models.Model):
    class Meta:
        verbose_name = "Пользователи"
        verbose_name_plural = "Пользователи"
        db_table = "user"

    name = models.CharField(max_length=100,
                            verbose_name="Имя пользователя")
    login = models.CharField(max_length=100,
                             verbose_name="Логин")
    password = models.CharField(max_length=1000,
                                verbose_name="Пароль")