# Generated by Django 3.1.7 on 2021-03-26 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField(unique=True)),
                ('name_of_type', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Типы',
                'verbose_name_plural': 'Типы',
                'db_table': 'types',
            },
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=5000, verbose_name='Текст записи')),
                ('slug_address', models.CharField(blank=True, max_length=100, null=True, verbose_name='адрес записи')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='note_author', to='users.user', verbose_name='Автор записи')),
                ('type_of_text', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notes.type', verbose_name='Тип записи')),
            ],
            options={
                'verbose_name': 'Записи',
                'verbose_name_plural': 'Записи',
                'db_table': 'note',
            },
        ),
    ]
