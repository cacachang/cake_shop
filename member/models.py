from django.db import models
from django.urls import reverse

# Create your models here.

class User(models.Model):
  name = models.CharField(max_length=10)
  age = models.IntegerField()
  email = models.CharField()
  address = models.CharField()
  phone = models.CharField()

  def get_absolute_url(self):
        return reverse("index")