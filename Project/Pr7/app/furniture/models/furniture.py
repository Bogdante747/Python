from django.db import models

class Furniture(models.Model):
    label = models.CharField(max_length=255)
    photo = models.CharField(max_length=255)