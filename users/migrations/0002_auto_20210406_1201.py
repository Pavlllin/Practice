# Generated by Django 3.1.7 on 2021-04-06 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='user',
            index=models.Index(fields=['date'], name='date_user_idx'),
        ),
    ]
