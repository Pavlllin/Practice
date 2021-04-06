from django.db import models


# Create your models here.
class Note(models.Model):
    text = models.CharField(max_length=5000,
                            verbose_name="Текст записи")
    title = models.CharField(max_length=100,
                             verbose_name="Название записи")
    author = models.ForeignKey('users.User', on_delete=models.CASCADE,
                               verbose_name="Автор записи", related_name="note_author")

    slug_address = models.CharField(max_length=100,
                                    verbose_name="адрес записи",
                                    null=True,
                                    blank=True)

    type_of_text = models.ForeignKey('notes.Type', on_delete=models.CASCADE,
                                     verbose_name="Тип записи", null=False)

    date = models.DateTimeField(verbose_name="Дата создания",auto_now_add=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Записи"
        verbose_name_plural = "Записи"
        db_table = "note"
        indexes = [
            models.Index(fields=['text'], name='text_idx'),
            models.Index(fields=['date'],name='date_note_idx'),
        ]


class Type(models.Model):
    type = models.IntegerField(unique=True)
    name_of_type = models.CharField(max_length=100)

    def __str__(self):
        return self.name_of_type

    class Meta:
        verbose_name = "Типы"
        verbose_name_plural = "Типы"
        db_table = "types"
        indexes = [
            models.Index(fields=['name_of_type'], name='name_idx')
        ]

