from django.db import models


# Create your models here.
class Note(models.Model):
    text = models.CharField(max_length=5000,
                            verbose_name="Текст записи")
    author = models.ForeignKey('users.User', on_delete=models.CASCADE,
                               verbose_name="Автор записи", related_name="note_author")

    slug_address = models.CharField(max_length=100,
                                    verbose_name="адрес записи",
                                    null=True,
                                    blank=True)

    type_of_text = models.ForeignKey('notes.Type', on_delete=models.CASCADE,
                                     verbose_name="Тип записи", null=False)

    def __str__(self):
        return self.text[:50]

    class Meta:
        verbose_name = "Записи"
        verbose_name_plural = "Записи"
        db_table = "note"


class Type(models.Model):
    type = models.IntegerField(unique=True)
    name_of_type = models.CharField(max_length=100)

    def __str__(self):
        return self.name_of_type

    class Meta:
        verbose_name = "Типы"
        verbose_name_plural = "Типы"
        db_table = "types"

