# Generated by Django 3.1.7 on 2021-03-11 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210311_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='login',
            field=models.CharField(max_length=100, verbose_name='Логин'),
        ),
    ]
