# Generated by Django 3.1.7 on 2021-04-07 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210406_1201'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='count_notes',
            field=models.IntegerField(default=0, verbose_name='Кол-во записей пользователя'),
        ),
    ]