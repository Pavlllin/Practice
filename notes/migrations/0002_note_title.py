# Generated by Django 3.1.7 on 2021-03-30 11:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='title',
            field=models.CharField(default=django.utils.timezone.now, max_length=100, verbose_name='Название записи'),
            preserve_default=False,
        ),
    ]
