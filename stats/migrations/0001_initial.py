# Generated by Django 3.1.7 on 2021-03-26 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя статистики')),
                ('result', models.IntegerField(verbose_name='Результат статистики')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Создана в ')),
            ],
            options={
                'verbose_name': 'Статистика',
                'verbose_name_plural': 'Статистика',
                'db_table': 'Stats',
            },
        ),
        migrations.CreateModel(
            name='TypeStats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=50, unique=True)),
            ],
        ),
    ]
