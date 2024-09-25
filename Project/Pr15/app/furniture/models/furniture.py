from django.db import models

class Furniture(models.Model):
    label = models.CharField(max_length=255)
    image = models.ImageField(upload_to="furniture/%Y/%m/%d")
    price = models.IntegerField()