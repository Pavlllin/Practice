from django.db import models


# Create your models here.
class Note(models.Model):
    class Meta:
        verbose_name = "Записи"
        verbose_name_plural = "Записи"
        db_table = "note"

    text = models.CharField(max_length=5000,
                            verbose_name="Текст записи")
    author = models.ForeignKey('notes.User', on_delete=models.CASCADE,
                               verbose_name="Автор записи")
    address = models.ForeignKey('notes.Address', on_delete=models.CASCADE,
                                 verbose_name="адрес записи", null=True)


class Address(models.Model):
    class Meta:
        verbose_name = "Ссылки"
        verbose_name_plural = "Ссылки"
        db_table = "address"

    slug_url = models.SlugField(null=True)


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

# модель(слаг)+
# Длина +
# Мета(verbose + plural, table_name) +
# ссылки в нотах +
