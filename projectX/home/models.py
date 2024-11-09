from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(max_length=100)
    address = models.TextField(null=True, blank=True)
    image = models.ImageField()
    file = models.FileField()
  