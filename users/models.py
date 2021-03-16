from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100,
                            verbose_name="Имя пользователя")
    login = models.CharField(max_length=100,
                             unique=True,
                             verbose_name="Логин")
    password = models.CharField(max_length=1000,
                                verbose_name="Пароль")
    def __str__(self):
        return self.login

    class Meta:
        verbose_name = "Пользователи"
        verbose_name_plural = "Пользователи"
        db_table = "user"