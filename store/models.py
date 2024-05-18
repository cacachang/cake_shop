from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20, default="")

class Specification(models.Model):
    flavor = models.CharField(max_length=20, default="")
    size = models.IntegerField(max_length=20, default=0)

class Product(models.Model):
    name = models.CharField(max_length=20, default="")
    price = models.DecimalField(default=0, decimal_places=1, max_digits=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    specification = models.ForeignKey(Specification, on_delete=models.CASCADE)
