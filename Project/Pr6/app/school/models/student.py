from django.db import models
from .course import Course

class Student(models.Model):
    name = models.CharField(max_length=100)
    course = models.ManyToManyField(Course)