from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=150)
    second_name = models.CharField(max_length=150)
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=150)

