from django.db import models

# Create your models here.

class Product(models.Model):

    name = models.CharField(max_length=200)
    price = models.CharField(max_length=10)
    description = models.CharField(max_length=250)
    manufacurer = models.CharField(max_length=250)
    category = models.CharField(max_length=30)

    class Meta:
        ordering = ['name']
