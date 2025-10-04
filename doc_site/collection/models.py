from django.db import models

# Create your models here.
class Entry(models.Model):
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=50, unique=True)
    