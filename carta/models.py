from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200, default="")
    description = models.CharField(max_length=1000, default="")
    img = models.URLField()

