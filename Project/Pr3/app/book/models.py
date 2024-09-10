from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=10)
    year = models.IntegerField()

class Author(models.Model):
    name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=255)