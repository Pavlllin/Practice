from django.db import models

# Create your models here.
class UserStats(models.Model):
    user = models.CharField(max_length=100)