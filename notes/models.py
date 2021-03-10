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

    slug_address = models.CharField(max_length=100,
                                    verbose_name="адрес записи",
                                    unique=True,
                                    null=True)

    type_of_text = models.ForeignKey('notes.Types', on_delete=models.CASCADE,
                                     verbose_name="Тип записи", null=True)


class Types(models.Model):
    class Meta:
        verbose_name = "Типы"
        verbose_name_plural = "Типы"
        db_table = "types"

    type = models.IntegerField(unique=True)
    name_of_type = models.CharField(max_length=100)


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

# модель(тип)+
# Длина +
# Мета(verbose + plural, table_name) +
# ссылки в нотах +
