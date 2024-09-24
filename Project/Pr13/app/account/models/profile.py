from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.forms import ModelForm

class Gender(models.TextChoices):
    MEN = "Мужской"
    WOMEN = "Женский"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(choices=Gender, blank=True, max_length=20)

    country = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    street = models.CharField(max_length=100, blank=True)
    house = models.CharField(max_length=100, blank=True)
    apartment_number = models.CharField(max_length=100, blank=True)

    def get_absolute_url(self):
        return reverse('home')